from disco.bot import Plugin


class Listener(Plugin):
    @Plugin.listen('MessageCreate')
    def on_create_msg_listen(self, event):
        print(dir(event.message))
