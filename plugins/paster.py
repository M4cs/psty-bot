import requests, json, io
from PIL import Image

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
        
    def upload_file(self, file_url, language="plaintext"):
        data = requests.get(file_url).content
        img = Image.open(io.BytesIO(data))
        res = self.sesh.post(self.url, data={
            'file': img,
            'lang': language
        })
        print(res.content)
