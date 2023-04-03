import json
from flask import Flask, jsonify, request
from main.factories.signUp import makeSignUp
from presentation.controllers.protocols.http import HttpRequest


app = Flask(__name__)


@app.route("/user", methods=["POST"])
async def index():
    record = json.loads(request.data)
    httprequest = HttpRequest(body=record)
    controller = makeSignUp()
    result = await controller.handle(httprequest)
    return jsonify(result.body.toDict())


app.run(host="0.0.0.0", port=3000)
