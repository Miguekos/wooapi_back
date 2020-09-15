from app import app
from flask import jsonify, flash, request
import logging
import requests
import json


@app.route('/olva', methods=['POST'])
def enviOlva():
    _json = request.json
    try:
        # Cuerpo de Olva
        body_json = {
            "consignado": _json['consignado'],
            "nroDocConsignado": _json['nroDocConsignado'],
            "direccion": _json['direccion'],
            "ubigeo": _json['ubigeo'],
            "codigoRastreo": _json['codigoRastreo'],
            "observacion": _json['observacion'],
            "montoArticulo": _json['montoArticulo'],
            "receptor": _json['receptor'],
            "rucSeller": _json['rucSeller'],
            "ubigeoSeller": _json['ubigeoSeller'],
            "seller": _json['seller'],
            "direccionSeller": _json['direccionSeller'],
            "contacto": _json['contacto'],
            "telefono": _json['telefono'],
            "codClienteRucDni": _json['codClienteRucDni'],
            "total": _json['total'],
            "formaPago": _json['formaPago'],
            "tipoEnvio": _json['tipoEnvio'],
            "altoEnvio": _json['altoEnvio'],
            "anchoEnvio": _json['anchoEnvio'],
            "largoEnvio": _json['largoEnvio'],
            "pesoUnitario": _json['pesoUnitario'],
            "codContenedor": _json['codContenedor']
        }

        # Servicio de Olva
        headersOlva = {'Content-Type': 'application/json', 'tokenSeguridad' : 'ZwJ7cwBg549F64VAqE8R2xACOmosjkMJN7IsTP0CwvQM4krK1nU4cg=='}
        response = requests.put('http://wap.olvacourier.com:8080/RegistroRemito-1.0-SNAPSHOT/webresources/remito/generar',
                                data=json.dumps(body_json), headers=headersOlva)
        rs = response.json()
        if rs['lista'] == []:
            return rs
        else:
            jsonError = {
                "jsonError": rs['lista']
            }
            return jsonify(jsonError)
    except ValueError:
        print(ValueError)
