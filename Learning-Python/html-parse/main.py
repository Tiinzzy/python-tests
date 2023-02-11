from flask import Flask, jsonify
from phil import get_all_data

app = Flask(__name__)


@app.route("/all-relationships")
def all_relationships():
    data = get_all_data()
    return jsonify(data)


@app.route("/send-data-to-frontend")
def send_relationships():
    data = get_all_data()
    return jsonify(data)


# if __name__ == "__main__":
#     data = get_all_data()
#     print(data)
