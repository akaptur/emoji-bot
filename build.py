def clean_file():
    with open('emojis.txt', 'rw') as f:
        emojis = f.readlines()

        if not emojis[0].startswith(":"):
            processed = "\n".join([":" + em.strip() + ":" for em in emojis])
            with open('cleaned_emoji.txt', 'w') as g:
                g.write(processed)

def build_message():
    with open('cleaned_emoji.txt', 'r') as f:
        emojis = f.readlines()
    return "  ".join(["`"+em+"` ,"+em for em in emojis]) # `:foo:` :foo:
