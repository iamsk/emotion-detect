import requests

from config import KEY


def detect(_file):
    if isinstance(_file, str):
        content_type = 'application/json'
        d = {'json': {"url": _file}}
    else:
        content_type = 'application/octet-stream'
        d = {'data': _file}
    headers = {'Content-Type': content_type, 'Ocp-Apim-Subscription-Key': KEY}
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'
    res = requests.post(url=face_api_url, params=params, headers=headers, **d).json()
    if isinstance(res, dict):
        return res
    return res[0]['faceAttributes']['emotion']


if __name__ == '__main__':
    url = 'https://how-old.net/Images/faces2/main007.jpg'
    print detect(url)
