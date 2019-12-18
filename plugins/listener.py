from disco.bot import Plugin
from plugins.paster import Paster

paster = Paster()

class Listener(Plugin):
    @Plugin.listen('MessageCreate')
    def on_create_msg_listen(self, event):
        print(dir(event.message))
        print(dir(event))
        print(event.raw_data)
        print(event.message)
        urls = []
        if len(event.raw_data['message']['attachments']) != 0:
            for attachment in event.message.raw_data['message']['attachments']:
                urls.append(attachment['url'])
        for url in urls:
            paster.upload_file(url)

