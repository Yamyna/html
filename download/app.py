from flask import Flask, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/html/virus'
ALLOWED_EXTENSIONS = {'exe', 'dll', 'pdf', 'docx', 'xlsx'}  # Ajoutez les extensions que vous voulez autoriser

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Lancer le script bash après le téléchargement
        subprocess.run(['/var/www/html/docker_script.sh', filename])
        return 'File uploaded and docker script executed'
    return 'File type not allowed'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)