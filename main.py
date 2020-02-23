from flask import Flask, send_file, request
import blurhash
import PIL
import PIL.Image
import numpy as np
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/process', methods=['POST'])
def processImage():
    file = request.files['file']
    width = int(request.form.get('width', 128))
    height = int(request.form.get('height', 128))

    image = np.array(PIL.Image.open(file).convert("RGB"))
    blur_hash = blurhash.encode(np.array(image))

    img = PIL.Image.fromarray(np.array(blurhash.decode(blur_hash, width, height)).astype('uint8'))

    fp = tempfile.NamedTemporaryFile(delete=False)
    img.save(fp, format='PNG')
    fp.close()
    return send_file(fp.name, mimetype='image/png')

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')