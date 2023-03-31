import json
from flask import Flask, jsonify, request

from src.entities.user import User

app = Flask(__name__)


@app.route("/user", methods=["POST"])
def index():
    record = json.loads(request.data)
    print(record)
    user = User(
        record["id"],
        record["fullname"],
        record["email"],
        record["password"],
    )
    return jsonify(user.toJSON())


app.run(host="0.0.0.0", port=3000)
