import json
import os
import tempfile
from flask import Flask, abort, request, redirect, render_template
app = Flask(__name__)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/storage/json/all', methods=['GET'])
def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


@app.route('/api/v1/storage/json', methods=['GET'])
def get():
    key = request.args.get('key')
    data = get_data()
    if key in data:
        return data.get(key)
    else:
        return ''


@app.route('/api/v1/storage/json/write', methods=['GET', 'POST'])
def put():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.json
        for k, v in json_data.items():
            key = k
            value = v
    else:
        key = request.args.get('key')
        value = request.args.get('val')
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))
    return redirect('/api/v1/storage/json/all')


if __name__ == '__main__':
    app.run()
