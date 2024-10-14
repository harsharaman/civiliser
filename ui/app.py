from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def upload_files():
    return render_template('upload_files.html')

DATA_DIR_PATH = "./data"
RESUME_FILES_PATH = os.path.join(DATA_DIR_PATH, "resumes")

@app.route('/upload', methods=['POST'])
def handle_uploads():
    if not os.path.exists(DATA_DIR_PATH):
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
        os.makedirs(RESUME_FILES_PATH, exist_ok=True)

    # Retrieve the uploaded files
    resumes = request.files.getlist('resumes')
    jd = request.files['job_description']

    # Check if the files are actually uploaded
    if not jd or jd.filename == "":
        flash("Please upload the required files - Job Description and Resumes")
        return redirect(url_for('upload_files'))
    
    # Save files to a directory and save the paths
    filepath_jd = os.path.join(DATA_DIR_PATH, jd.filename)
    jd.save(filepath_jd)

    filepaths_resumes = []
    for resume in resumes:
        filepath_resume = os.path.join(RESUME_FILES_PATH, resume.filename)
        resume.save(filepath_resume)
        filepaths_resumes.append(filepath_resume)

    print('INFO - Uploaded files saved')
    return render_template('thanks.html')


if __name__=="__main__":
    app.run(debug=True)