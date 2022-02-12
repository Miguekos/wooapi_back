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
from apiwoo import wcapi
from funciones import ValidaComuna
# from wooapi import wcapi
# import atuGobPe
from database.mongodb import mycolnew, mycol

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
    # cupones = wcapi.get("coupons", params={"per_page": 100, "id" mongolva: 1}).json()
    cupones = wcapi.get("coupons").json()
    return jsonify(cupones)
    # return "{}".format(asd)


@app.route('/ordenes/<page>/<limit>', methods=['GET'])
def woocommerce_ordenes(page, limit):
    # asd = wcapi.options("orders").json()
    # asd = wcapi.get("search").json()
    ordenes = []
    d = 0
    while d < int(page):
        ordenes.extend(wcapi.get("orders", params={"page": d + 1, "per_page": limit}).json())
        # print("pagina", d + 1)
        d = d + 1
    # print(ordenes)
    # print(len(ordenes))
    # print(type(ordenes))
    new_json_response = []
    x = mycol.find({}, projection={"_id" : 0, "idpedido":1})
    idpedidos = []
    for d in  list(x):
        idpedidos.append(d['idpedido'])

    # print("resultStr", idpedidos)
    for pedidos in ordenes:
        validar = ValidaComuna(pedidos, idpedidos)
        response = validar.logica_validations()
        # print(response)
        new_json_response.append(response)
    return jsonify(new_json_response)
    # return "{}".format(asd)


@app.route('/ordenes/<id>', methods=['GET'])
def woocommerce_orden_id(id):
    asd = wcapi.get("orders/{}".format(id), params={"per_page": 100}).json()
    return jsonify(asd)

@app.route('/estatus/', methods=['GET'])
def woocommerce_status():
    response = wcapi.get("system_status").json()
    return jsonify(response)

@app.route('/ordenes/<id>/<idolva>', methods=['PUT'])
def woocommerce_orden_update(id, idolva):
    getPro = wcapi.get("orders/{}".format(id)).json()
    for asd in getPro['meta_data']:
        if (asd['key'] == "_wc_shipment_tracking_items"):
            asd['value'][0]['tracking_number'] = idolva
            asd['value'][0]['tracking_provider'] = "Olva"
            # print(asd['value'][0]['tracking_number'])
    # print(getPro['meta_data'][6]['value'][0])
    # print(getPro['meta_data'])
    data = {
        "status": "despachado",
        "meta_data": getPro['meta_data']
    }
    response = wcapi.put("orders/{}".format(id), data).json()
    return jsonify(response)

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8050, debug=True)
