"""
This module creates the code. It's independent of bot.py so the code doesn't
change every time the bot is activated, but the code is still mutable by
running this module.
"""

import string
import random
import json

with open('cleaned_emoji.txt', 'r') as f:
    full_emoji_list = [em.strip() for em in f.readlines()]

code_dictionary = dict(zip(string.ascii_lowercase,
    [random.choice(full_emoji_list) for _ in range(len(string.ascii_lowercase))]))

with open('emoji_code.txt', 'w') as f:
    json.dump(code_dictionary, f)