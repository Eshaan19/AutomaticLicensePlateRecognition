from flask import Flask, render_template, request, url_for
from PIL import Image
import numpy as np
import cv2
import io
import base64

import extract

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = 'D:/Python/final_project/static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/templates/application.html", methods=['GET', "POST"])
def application():
    if request.method == 'POST' and 'file' in request.files:
        photo = request.files['file']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        text, state = extract.extract(img)
        path = "D:/Python/final_project/static/data.jpeg"
        path2 = "/static/data.jpeg"

        cv2.imwrite(path, img)
        return render_template("application.html",text=text,state=state,path=path2)
    
    return render_template("application.html")

if __name__ == "__main__":
    app.run()
