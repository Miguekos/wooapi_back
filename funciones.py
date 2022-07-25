from fuzzywuzzy import fuzz
from datetime import datetime

class ValidaComuna():
    def __init__(self, obj, arg, tipo_pago, comunas):
        self.json_ = obj
        self.arg_ = arg
        self.tipo_pago_ = tipo_pago
        self.comunas_ = comunas

    def logica_validations(self):
        # print("self.json_->", self.json_)
        # print("self.arg_->", self.arg_)
        # n2 = "saNtiaop"
        numero = 0
        comuna = ''
        precio = ''

        def search(name, people):
            return [element for element in people if element['id'] == name]

        for comunas in self.comunas_:
            valor = fuzz.ratio(comunas['name'].lower(), self.json_['billing']['city'].lower())
            if valor > numero:
                numero = valor
                comuna = comunas['name']
                precio = comunas['provee']
                # print('precio-->', comunas['provee'])
            if self.json_['id'] in self.arg_:
                self.json_['enviado'] = True
                self.json_['tipodepago'] = search(self.json_['id'], self.tipo_pago_)[0]['tipo']
            else:
                self.json_['enviado'] = False
                self.json_['tipodepago'] = 'Por pagar'

        # print(numero)
        # print(comuna)
        self.json_['billing']['city_ori'] = self.json_['billing']['city']
        self.json_['billing']['porcentaje'] = numero
        self.json_['billing']['city'] = comuna
        self.json_['precio'] = precio
        fecha = datetime.strptime(self.json_['date_created'], '%Y-%m-%dT%H:%M:%S')

        # print("fecha-->", fecha.strftime("%d/%m/%Y"))
        self.json_['fecha_registro'] = fecha.strftime("%d/%m/%Y %H:%M")
        return self.json_
