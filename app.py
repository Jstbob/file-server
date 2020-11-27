from flask import request, Flask, send_from_directory, url_for, jsonify
import uuid, os, datetime

basepath = r'C:\download'
app = Flask(__name__)


@app.route('/u/upload/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(basepath, filename=filename, as_attachment=True)

@app.route('/u/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    filename = str(uuid.uuid4()) + '.log'
    upload_path = os.path.join(basepath, filename)
    while os.path.exists(upload_path):
        filename = str(uuid.uuid4()) + '.log'
        upload_path = os.path.join(basepath, filename)
    f.save(upload_path)
    url = url_for('upload_file', _external=True) + '/' + filename
    return jsonify({'url': url})

@app.route('/u/getDate',methods=['POST','GET'])
def getDate():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/u/getUTCDate',methods=['POST','GET'])
def getUTCDate():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run()
