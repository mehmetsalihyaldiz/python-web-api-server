from flask import Flask,  render_template, json, jsonify, make_response
import os
import json
import io

app = Flask(__name__)

@app.route("/api/<int:this_number>", methods=['GET'])
def api(this_number):
    f = io.open("uploads/data/data.json", mode="r", encoding="utf-8")
    data = json.loads(f.read())
    r = make_response(json.dumps(data[:this_number], indent=4))
    r.mimetype = 'application/json'
    return r


@app.route('/api/', methods=['GET'])
def all():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "uploads/data", "data.json")
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
