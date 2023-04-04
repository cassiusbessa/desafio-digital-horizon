import json
from flask import Flask, jsonify, request
from main.factories.listUsers import makeListUsers
from main.factories.login import makeLogin
from main.factories.signUp import makeSignUp
from presentation.controllers.protocols.http import HttpRequest


app = Flask(__name__)


@app.route("/users", methods=["POST"])
async def index():
    record = json.loads(request.data)
    httpRequest = HttpRequest(body=record)
    controller = makeSignUp()
    result = await controller.handle(httpRequest)
    return jsonify(result.body)


@app.route("/login", methods=["POST"])
async def login():
    if len(request.data) == 0:
        return jsonify({"error": "empty body"})
    record = json.loads(request.data)
    httpRequest = HttpRequest(body=record)
    controller = makeLogin()
    result = await controller.handle(httpRequest)
    return jsonify(result.body)


@app.route("/users", methods=["GET"])
async def listUsers():
    controller = makeListUsers()
    httpRequest = HttpRequest()
    if request.headers.get("Authorization") is None:
        return jsonify({"error": "missing authorization header"})
    httpRequest.headers = request.headers
    result = await controller.handle(httpRequest)
    return jsonify(result.body)
