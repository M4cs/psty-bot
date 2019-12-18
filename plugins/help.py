from disco.bot import Plugin

class Help(Plugin):
    @Plugin.command('help')
    def on_help_command(self, event):
        event.msg.reply("""$paste <language or plaintext> <content>""")
