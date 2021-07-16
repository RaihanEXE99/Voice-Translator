from flask import Flask, request, render_template,send_file,send_from_directory
from werkzeug.utils import secure_filename
import os

from processing import generateOutput
import os
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def my_page():
    if request.method == "POST":
        f = request.files.get("file")
        ext = request.form.get("ext")
        language = request.form.get("language")

        if f:
            filename = secure_filename(f.filename)
            file_path = os.path.join('temp_files', filename)
            f.save(file_path)
            output_data = generateOutput(file_path,language,ext)

            if output_data=="Error, Something Wrong!":
                return render_template('error.html',err_body=output_data)

            txt_filename = filename[:-4]+"."+ext
            return render_template('index.html', output=output_data, flag=1, filename=txt_filename)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
