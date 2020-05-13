from app import app
from flask import jsonify, flash, request
import logging
import requests
import json
from database.mongodb import mycol
from flask_cors import CORS
import utils.logs
import logging
CORS(app, supports_credentials=False)


@app.route('/mongolva', methods=['POST', 'GET'])
def mongolvapost():
    if (request.method == "POST"):
        _json = request.json
        logging.debug("POST")
        logging.debug(_json)
        logging.debug("POST")
        print(_json)
        x = mycol.insert(_json)
        resp = jsonify('{}'.format(x))
        resp.status_code = 200
        return resp
    elif (request.method == "GET"):
        x = mycol.find({},{ "_id": 0})
        resultStr = list(x)
        logging.debug("PeticionGET: {}".format(resultStr))
        return jsonify(resultStr)