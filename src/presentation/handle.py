import json
from flask import Flask, jsonify, request

from src.domain.entities.user import User


app = Flask(__name__)


@app.route("/user", methods=["POST"])
def index():
    record = json.loads(request.data)
    user = User(
        id=record["id"],
        fullname=record["fullname"],
        email=record["email"],
        password=record["password"],
    )
    return jsonify(user.toJSON())


app.run(host="0.0.0.0", port=3000)
