## Emoji-bot

An emoji bot for Zulip.

### Commands
Emoji bot only responds to PMs, so you can only annoy yourself.

#### Random
Say anything to the bot to get ten random emojis.

#### ALL THE EMOJIS
Say "ALL THE EMOJIS" to the bot to get all the emojis back in a single message.  WARNING: This will slow down your Zulip noticeably.

#### Translate
Say "Translate" with a message to the bot to get your message back with emoji-commands turned into actual emojis. (Ex: "translate smile" will return the smile emoji.)

#### Encrypt
Say "Encrypt" to the bot to get your message encrypted in emojis. (Ex: "hello world" will return an encrypted string where individual letters have been replaced with their randomly chosen emoji counterparts.)

#### Decrypt
Say "Decrypt" to the bot to get an emoji-encrypted message (see above) returned in plaintext.

##Contributing

Emoji bot used a little javascript to scrape all the emoji-autocompletes into a text file. (You can run this, but it takes about half an hour.)

The bot is written in Python with requests.  Add new conversation by editing parse_and_dispatch and adding the appropriate functions.  See the issues page for more.
