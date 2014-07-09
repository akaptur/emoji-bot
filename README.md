## Emoji-bot

An emoji bot for Zulip.

### Commands
Emoji bot only responds to PMs, so you can only annoy yourself.

#### ALL THE EMOJIS
Say "ALL THE EMOJIS" to the bot to get all the emojis back in a single message.  WARNING: This will slow down your Zulip noticeably.

#### LEARN ME EMOJIS
Say "LEARN ME EMOJIS" to the bot to get ten random emojis.

#### Translate
Say "Translate" with a message to the bot to get your message back with emoji-commands turned into actual emojis. (Ex: "translate smile" will return the smile emoji.)

#### Everything Else
Say anything else to the bot to get your message returned in emoji code.

##Contributing

Emoji bot used a little javascript to scrape all the emoji-autocompletes into a text file. (You can run this, but it takes about half an hour.)

The bot is written in Python with requests.  Add new conversation by editing parse_and_dispatch and adding the appropriate functions.  See the issues page for more.
