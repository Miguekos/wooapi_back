# -*- coding: utf-8 -*-
# import dotenv
import os
from pathlib import Path  # python3 only
import sys
from app import app
import json
import unicodedata
from flask_cors import CORS
# from bson.objectid import ObjectId
# from bson.json_util import dumps
# from pymongo import MongoClient
import re
from unicodedata import normalize
# from test import ScraperSunarpPlacaPropietario
from flask import Flask, request, jsonify
from euphoria import wcapi
# import atuGobPe

CORS(app, supports_credentials=True)

@app.route('/productos', methods=['GET', 'POST'])
def woocommerce_product():
    json = request.get_json()
    # print(json['registros'])
    # asd = wcapi.get("products", params={"per_page": json['registros']}).json()
    asd = wcapi.get("products", params={"per_page": 100}).json()
    print(asd)
    print(len(asd))
    print(type(asd))
    return jsonify(asd)
    # return "{}".format(asd)

@app.route('/ordenes', methods=['GET', 'POST'])
def woocommerce_ordenes():
    json = request.get_json()
    print(json['registros'])
    asd = wcapi.get("orders", params={"per_page": 100}).json()
    print(asd)
    print(len(asd))
    print(type(asd))
    return jsonify(asd)
    # return "{}".format(asd)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=6000, debug=True)
