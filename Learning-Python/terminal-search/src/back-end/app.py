from flask import Flask, request, jsonify
import json

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/db/mongodb/connect', methods=["POST"])
def connect_mongo_db():
    pass
