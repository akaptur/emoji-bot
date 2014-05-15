import requests
import os
import sys
import random
import json
import re
import pdb
import build

build.clean_file()
all_emojis = build.build_message()

class Bot(object):
    """ All the emojis."""
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

        self.register_for_messages()

    def register_for_messages(self):
        params = {"event_types" : ['messages']}
        r = requests.post(self.register_url, auth=self.bot_auth, params=json.dumps(params))
        self.q_id = r.json()['queue_id']

    def listen_on_queue(self):
        params = {"queue_id": self.q_id, "last_event_id": self.last_event_id}
        r = requests.get(self.events_url, auth=self.bot_auth, params=params)
        print r.content
        return r.json()
        # pdb.set_trace()

    def post_emojis(self):
        all_emojis_list = all_emojis.split(" ")
        size = len(all_emojis_list)
        start = random.randint(0,size)
        some_emojis = " ".join(all_emojis_list[start:start+20])
        params = {"type": "private",
                  "to": "allison@hackerschool.com",
                  "content": some_emojis}
        r = requests.post(self.message_url, auth=self.bot_auth, params=params)
        print r.content
        print r.request.url
        pdb.set_trace()

    def post_yay_message(self, gif, person_to_ping, subject, stream, msg_type="stream"):
        if self.muted:
            return
        if person_to_ping:
            person_to_ping = "@**" + person_to_ping + "**"

        params = {
            "type" : msg_type,
            "content" : person_to_ping + " [Yay!]("+ gif + ")" + '\n' + "[(about me)]("+ self.about_me + ")",
            "to" : stream,
            "subject" : subject,
            }
        r = requests.post(self.post_url, params=params, auth=self.bot_auth)
        # TODO: logging on error
        return r


    def get_recipients(self, message):
        """ Return the properly encoded string of email addresses that received a message."""
        emails = [r["email"] for r in message["display_recipient"]]
        return json.dumps(emails)


if __name__ == "__main__":
    b = Bot()

    while True:
        messages = b.listen_on_queue()
        if messages:
            for m in messages:
                b.post_emojis()
