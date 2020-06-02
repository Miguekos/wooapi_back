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
# from wooapi import wcapi
# import atuGobPe
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def woocommerce_home():
    return jsonify("Dev WooComerceApiPython")

@app.route('/productos/<limit>', methods=['GET'])
def woocommerce_product(limit):
    productos = wcapi.get("products", params={"per_page": limit}).json()
    # print(productos)
    # print(len(productos))
    # print(type(productos))
    return jsonify(productos)
    # return "{}".format(asd)

@app.route('/productos/<id>', methods=['GET'])
def woocommerce_product_id(id):
    asd = wcapi.get("products/{}".format(id), params={"per_page": 100}).json()
    return jsonify(asd)

@app.route('/cupones', methods=['GET'])
def woocommerce_cupones():
    # json = request.get_json()
    # print(json['registros'])
    # asd = wcapi.get("products", params={"per_page": json['registros']}).json()
    # cupones = wcapi.get("coupons", params={"per_page": 100, "id" : 1}).json()
    cupones = wcapi.get("coupons").json()
    return jsonify(cupones)
    # return "{}".format(asd)

@app.route('/ordenes/<limit>', methods=['GET'])
def woocommerce_ordenes(limit):
    # asd = wcapi.options("orders").json()
    # asd = wcapi.get("search").json()
    ordenes = wcapi.get("orders", params={"per_page": limit}).json()
    # print(ordenes)
    # print(len(ordenes))
    # print(type(ordenes))
    return jsonify(ordenes)
    # return "{}".format(asd)

@app.route('/ordenes/<id>', methods=['GET'])
def woocommerce_orden_id(id):
    asd = wcapi.get("orders/{}".format(id), params={"per_page": 100}).json()
    return jsonify(asd)



if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8050, debug=True)
