import requests
import os
import sys
import random
import json
import re
import pdb
import build

# build.clean_file()

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
            self.emojis = [em.strip() for em in f.readlines()]

        # With text: `:foo:` :foo:
        self.emojis_with_text = ["`"+em+"` "+em for em in self.emojis]

        self.register_for_messages()

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
                    print event
                    message = event['message']['content']
                    if "ALL THE EMOJI" in message:
                        self.post_all_emojis(sender)
                    else:
                        self.teach_some_emojis(sender)


    def teach_some_emojis(self, recipient):
        size = len(self.emojis_with_text)
        start = random.randint(0,size)
        some_emojis = "\n".join(self.emojis_with_text[start:start+11])

        params = {"type": "private",
                  "to": recipient,
                  "content": some_emojis}
        r = requests.post(self.message_url, auth=self.bot_auth, params=params)

    def post_all_emojis(self, recipient):
        string_emojis = "".join(self.emojis)
        params = {"type": "private",
                  "to": recipient,
                  "content": json.dumps(string_emojis)}
        r = requests.post(self.message_url, auth=self.bot_auth, data=params)
        print r.content
        print r.request.url


if __name__ == "__main__":
    b = Bot()

    while True:
        response = b.listen_on_queue()
        b.parse_and_dispatch(response)
