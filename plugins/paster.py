import requests, json

class Paster:
    def __init__(self):
        self.sesh = requests.session()
        self.url = 'https://psty.io/api'
    def paste_text(self, text, language="plaintext"):
        res = self.sesh.post(self.url, data={
            'code': text,
            'lang': language
        })
        content = res.json()
        if res.status_code == 200:
            return content['paste_link']
        else:
            return "Failed to paste your text! Sorry about that :("
