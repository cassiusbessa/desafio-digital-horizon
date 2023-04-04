import json
from flask import Flask, jsonify, request
from main.factories.login import makeLogin
from main.factories.signUp import makeSignUp
from presentation.controllers.protocols.http import HttpRequest


app = Flask(__name__)


@app.route("/user", methods=["POST"])
async def index():
    record = json.loads(request.data)
    httprequest = HttpRequest(body=record)
    controller = makeSignUp()
    result = await controller.handle(httprequest)
    return jsonify(result.body)


@app.route("/login", methods=["POST"])
async def login():
    if len(request.data) == 0:
        return jsonify({"error": "empty body"})
    record = json.loads(request.data)
    httprequest = HttpRequest(body=record)
    controller = makeLogin()
    result = await controller.handle(httprequest)
    return jsonify(result.body)
