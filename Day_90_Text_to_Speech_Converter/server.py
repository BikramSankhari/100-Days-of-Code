from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os, PyPDF2
from gtts import gTTS

UPLOAD_FOLDER = 'static/uploads/'
save_location = ''
saved_filename = ''

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret key'


@app.route("/")
def home():
    try:
        os.remove(save_location)
    except FileNotFoundError:
        pass
    return render_template("index.html", download=False)


@app.route('/download mp3')
def download():
    return render_template("index.html", download=True)


@app.route('/download')
def download_file():
    path = os.path.abspath('static/MP3s')
    return send_from_directory(path, saved_filename)


@app.route('/results', methods=["POST"])
def results():
    pdf_file = request.files['file1']
    if pdf_file and pdf_file.filename.rsplit('.')[1] == 'pdf':
        filename = secure_filename(pdf_file.filename)
        full_path_to_pdf = os.path.abspath(app.config['UPLOAD_FOLDER'] + filename)
        pdf_file.save(full_path_to_pdf)
        with open(full_path_to_pdf, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfReader(pdf)
            text_to_be_converted = ''
            for page_num in range(len(pdf_reader.pages)):
                text_to_be_converted += pdf_reader.pages[page_num].extract_text()
        os.remove(full_path_to_pdf)
        try:
            converted_mp3 = gTTS(text=text_to_be_converted, lang='en', slow=False)
        except AssertionError:
            flash('No text found in the PDF or the text in the PDF may be stored as images')
            return redirect(url_for('home'))
        else:
            global save_location, saved_filename
            saved_filename = filename.split('.')[0] + '.mp3'
            save_location = os.path.abspath('static/MP3s/' + saved_filename)
            converted_mp3.save(save_location)
        return redirect(url_for('download'))

    elif not pdf_file:
        flash('Please upload a PDF File to continue')
        return redirect(url_for('home'))
    else:
        flash('Please upload .pdf files only')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
