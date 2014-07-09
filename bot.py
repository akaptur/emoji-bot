import requests
import os
import sys
import random
import json
import re
import pdb
import build
from collections import namedtuple

Message = namedtuple('Message', 'text, sender')

class Bot(object):
    """ A bot to send you emojis. """
    def __init__(self):
        self.bot_name = "@**emojibot**"
        base_url = "https://zulip.com/api/v1/"
        self.register_url = base_url + "register"
        self.events_url = base_url + "events"
        self.message_url = base_url + "messages"

        humbug_key = os.environ["bot_key"]
        humbug_user = os.environ["bot_email"]
        self.bot_auth = (humbug_user, humbug_key)
        self.last_event_id = -1

        with open('cleaned_emoji.txt', 'r') as f:
            # [:foo:, :bar:, :baz:]
            self.emojis = [em.strip() for em in f.readlines()]

        self.emoji_words = [em[1:-1] for em in self.emojis]

        # With text: `:foo:` :foo:
        self.emojis_with_text = ["`"+em+"` "+em for em in self.emojis]

        self.register_for_messages()

    def start(self):
        while True:
            response = self.listen_on_queue()
            self.parse_and_dispatch(response)

    def register_for_messages(self):
        params = {"event_types" : ['messages']}
        r = requests.post(self.register_url, auth=self.bot_auth, params=json.dumps(params))
        self.q_id = r.json()['queue_id']

    def listen_on_queue(self):
        params = {"queue_id": self.q_id, "last_event_id": self.last_event_id}
        r = requests.get(self.events_url, auth=self.bot_auth, params=params)
        return r.json()

    def parse_and_dispatch(self, response):
        for event in response['events']:
            if event.has_key('message'):
                sender = event['message']['sender_email']
                b.last_event_id = event['message']['id']
                if sender != "emoji-bot@students.hackerschool.com":
                    msg = Message(event['message']['content'], event['message']['sender_email'])
                    self.dispatch_on(msg)

    def dispatch_on(self, message):
        if "ALL THE EMOJI" in message.text:
            self.post_all_emojis(message)
        elif "translate" in message.text.lower():
            self.translate(message)
        else:
            self.teach_some_emojis(message)

    def reply(self, recipient, content):
        params = {"type": "private",
                  "to": recipient,
                  "content": content}
        r = requests.post(self.message_url, auth=self.bot_auth, data=params)
        # print r.content
        # print r.request.url

    def teach_some_emojis(self, message):
        size = len(self.emojis_with_text)
        start = random.randint(0,size)
        some_emojis = "\n".join(self.emojis_with_text[start:start+11])
        self.reply(message.sender, some_emojis)

    def post_all_emojis(self, message):
        string_emojis = "".join(self.emojis)
        self.reply(message.sender, json.dumps(string_emojis))

    def translate(self, message):
        words = re.split(r'(\W+)', message.text)
        to_translate = words[(words.index('translate') + 1):]
        reply = []
        for word in to_translate:
            translation = self.match(word)
            if translation:
                reply.append(translation)
            else:
                reply.append(word)
        self.reply(message.sender, "".join(reply))

    def match(self, word):
        if word.lower() in self.emoji_words:
            return ":%s:" % word


if __name__ == "__main__":
    b = Bot()
    b.start()
