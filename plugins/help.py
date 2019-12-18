from disco.bot import Plugin

class Help(Plugin):
    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        if event.message.content == "@psty.io help":
            event.msg.reply("""$paste <language or plaintext> <content>""")
