from flask import Flask, render_template
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
import os, sys
import numpy as np
from PIL import Image

ALLOWED_EXTENSIONS = ['jpg', "jpeg", 'png']
UPLOAD_FOLDER = 'static/image/'


class Form(FlaskForm):
    file = FileField(label="Image", validators=[FileRequired(message="Please select an Image"),
                                                FileAllowed(ALLOWED_EXTENSIONS,
                                                            'Please Upload .jpg, .png or .jpeg Files only')])
    number = IntegerField(label="Select the number of Colors to be Extracted",
                          validators=[DataRequired(message="Please enter an Integer")])
    extract = SubmitField(label='Extract')

    def validate_number(self, number):
        if self.number.data < 1:
            raise ValidationError('Please Enter positive Integers Only')


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "Bikram"

file_path = ''


@app.route('/')
def home():
    form = Form()
    try:
        os.remove(file_path)
    except:
        pass
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    global file_path
    form = Form()
    if form.validate_on_submit():
        img = form.file.data
        number_of_colors = (0 - form.number.data)
        file_name = secure_filename(img.filename)
        file_path = os.path.abspath(app.config['UPLOAD_FOLDER'] + file_name)
        img.save(file_path)

        with Image.open(file_path) as image:
            arr = np.array(image)

        if arr.ndim == 3:
            unique_colors, unique_count = np.unique(arr.reshape(-1, arr.shape[2]), axis=0, return_counts=True)
            print(number_of_colors)
            top_rgb_colors = np.flip(unique_colors[unique_count.argsort()[number_of_colors:]], axis=0)
            print(top_rgb_colors)

            top_hex_colors = []
            for colors in top_rgb_colors:
                hex_code = '#'
                for color in colors:
                    hex_color = hex(color)[2:]
                    if len(hex_color) == 1:
                        hex_color = '0' + hex_color
                    hex_code += hex_color
                top_hex_colors.append(hex_code)

            print(top_hex_colors)
            return render_template('result.html', image=file_name, colors=top_hex_colors)

        else:
            return "<h1>It's a GrayScale Image. Nothing much to extract!!</h1>"
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
