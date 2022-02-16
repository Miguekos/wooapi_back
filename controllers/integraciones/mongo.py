from app import app
from flask import jsonify, flash, request
import logging
import requests
import json
from database.mongodb import mycol, mycolnew
from flask_cors import CORS
import utils.logs
import logging

CORS(app, supports_credentials=False)


@app.route('/mongolva', methods=['POST'])
def mongolvapost():
    _json = request.json
    logging.debug("POST")
    logging.debug(_json)
    logging.debug("POST")
    print(_json)
    x = mycol.insert(_json)
    resp = jsonify('{}'.format(x))
    resp.status_code = 200
    return resp

@app.route('/mongolva/<ini>/<fin>', methods=['GET'])
def mongolvaget(ini, fin):
        x = mycol.find({
            '0.id': { '$gte': int(ini), '$lte': int(fin)}
        }, {"_id": 0})
        resultStr = list(x)
        logging.debug("PeticionGET: {}".format(resultStr))
        return jsonify(resultStr)


@app.route('/envios/registro/add', methods=['POST'])
def envios_registro_add():
    _json = request.json
    # logging.debug("POST")
    # logging.debug(_json)
    # logging.debug("POST")
    print(_json)
    x = mycolnew.insert(_json)
    resp = jsonify('{}'.format(x))
    resp.status_code = 200
    return resp


@app.route('/envios/registro', methods=['GET'])
def envios_get_registros():
    x = mycolnew.find({}, {"_id": 0})
    resultStr = list(x)
    logging.debug("PeticionGET: {}".format(resultStr))
    return jsonify(resultStr)

@app.route('/envios/count', methods=['GET'])
def envios_total_registros():
    x = mycolnew.count()
    resultStr = x
    logging.debug("PeticionGET: {}".format(resultStr))
    return jsonify(resultStr)
