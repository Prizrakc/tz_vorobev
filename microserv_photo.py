# -*- coding: utf-8 -*-


from flask import Flask,request,send_file
import os
from convet import find
app  = Flask(__name__)


@app.route('/recognize',methods=['POST'])
def printing():
    a = os.path.basename(__file__)
    b = os.path.abspath(__file__).replace(a, '')
    final_file = b + "picture.jpeg" # ругается на путь, без
    jsn = request.get_json()
    picture_base64 = jsn['img']
    img, face_text = find(picture_base64,final_file)
    return send_file(final_file, mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug = True)