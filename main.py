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
from database.mongodb import mycolnew, mycol, mytexdevcomunas

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


@app.route('/ordenes/<page>/<limit>/<ini>/<fin>', methods=['GET'])
def woocommerce_ordenes(page, limit, ini, fin):
    comunas = mytexdevcomunas.find({}, projection={"_id": 0})
    comunas = list(comunas)
    # asd = wcapi.options("orders").json()
    # asd = wcapi.get("search").json()
    # ordenes = []
    # d = 0
    # while d < int(page):
    #     ordenes.extend(wcapi.get("orders", params={"include" : ['20307', '20308']}).json())
    #     # ordenes.extend(wcapi.get("orders", params={"page": d + 1, "per_page": limit, "parent": ['20307']}).json())
    #     # print("pagina", d + 1)
    #     d = d + 1
    # ordenes = wcapi.get("orders", params={"per_page": limit}).json()


    n1 = int(ini)
    n2 = int(fin)

    asd = n1

    while n1 < n2:
        # print(n1 + 1)
        asd = "{},{}".format(asd, n1 + 1)
        # print(asd)
        n1 = n1 + 1

    ordenes = []
    d = 0
    while d < int(page):
        ordenes.extend(wcapi.get("orders?include={}".format(asd), params={"page": d + 1, "per_page": limit}).json())
        # ordenes.extend(wcapi.get("orders", params={"page": d + 1, "per_page": limit, "parent": ['20307']}).json())
        # print("pagina", d + 1)
        d = d + 1

    # ordenes = wcapi.get("orders?include={}".format(asd), params={"per_page": limit}).json()

    print(ordenes)
    # print(len(ordenes))
    # print(type(ordenes))
    new_json_response = []
    x = mycol.find({}, projection={"_id": 0})
    idpedidos = []
    pedidos_tipo_pago = []
    for d in list(x):
        idpedidos.append(d['idpedido'])
        pedidos_tipo_pago.append({
            'id': d['idpedido'],
            'tipo': d['registro']['tipodepago']
        })
        # if d['registro']['tipodepago']:

    # print("resultStr", idpedidos)
    for pedidos in ordenes:
        validar = ValidaComuna(pedidos, idpedidos, pedidos_tipo_pago, comunas)
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
