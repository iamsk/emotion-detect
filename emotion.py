import httplib
import json
import requests

from config import KEY


def detect(_url):
    headers = {'Ocp-Apim-Subscription-Key': KEY}
    body = {"url": _url}
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize", json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print e
        return None


def detect2(_file):
    headers = {'Ocp-Apim-Subscription-Key': KEY, 'Content-Type': 'application/octet-stream'}
    res = requests.post(url='https://api.projectoxford.ai/emotion/v1.0/recognize', data=_file, headers=headers)
    return res.json()


if __name__ == '__main__':
    url = 'http://d31axo86ooexlu.cloudfront.net/moments/5644bb01d113f140d5ad985f_final.jpg'
    print detect(url)
