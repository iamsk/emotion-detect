import os
import time
import operator
from PIL import Image
from flask import Flask, render_template, request, jsonify

from emotion import detect2
from watermark import watermark_with_emotion

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path='/outputs', static_folder='outputs')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        f = request.files['photo']
        ret = detect2(f)
        if not ret:
            return jsonify(results=ret)
        scores = ret[0]['scores']
        sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
        emotion = sorted_scores[-1][0]
        im = Image.open(f)
        t = watermark_with_emotion(im, emotion)
        _p = 'outputs/%s.jpg' % time.time()
        output = os.path.join(CURRENT_PATH, _p)
        t.save(output, format='JPEG')
        return render_template('output.html', image_url='/%s' % _p)


if __name__ == "__main__":
    app.run()
