## Emoji-bot

An emoji bot for Zulip.

### Commands
Emoji bot only responds to PMs, so you can only annoy yourself.

#### Random
Say anything to the bot to get ten random emojis.

#### ALL THE EMOJIS
Say "ALL THE EMOJIS" to the bot to get all the emojis back in a single message.  WARNING: This will slow down your Zulip noticeably.


##Contributing

Emoji bot used a little javascript to scrape all the emoji-autocompletes into a text file. (You can run this, but it takes about half an hour.)

The bot is written in Python with requests.  Add new conversation by editing parse_and_dispatch and adding the appropriate functions.  See the issues page for more.
