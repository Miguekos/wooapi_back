from fuzzywuzzy import fuzz

lista_comunas = [

    {
        "name": "RANCAGUA"
    },

    {
        "name": "QUINTERO"
    },

    {
        "name": "LIMACHE"
    },

    {
        "name": "MACHALI"
    },

    {
        "name": "VILLA ALEMANA"
    },

    {
        "name": "MOSTAZAL"
    },

    {
        "name": "GRANEROS"
    },

    {
        "name": "OLIVAR"
    },

    {
        "name": "REQUINOA"
    },

    {
        "name": "RENGO"
    },

    {
        "name": "PLACILLA"
    },

    {
        "name": "CURAUMA"
    },

    {
        "name": "QUILPUE"
    },

    {
        "name": "CONCON"
    },

    {
        "name": "VALPARAÍSO"
    },

    {
        "name": "VIÑA DEL MAR"
    },

    {
        "name": "CURACAVÍ"
    },

    {
        "name": "CASABLANCA"
    },

    {
        "name": "ISLA DE MAIPO"
    },

    {
        "name": "COLINA"
    },

    {
        "name": "SANTIAGO"
    },

    {
        "name": "CONCHALI"
    },

    {
        "name": "QUILICURA"
    },

    {
        "name": "PUDAHUEL"
    },

    {
        "name": "PADRE HURTADO"
    },

    {
        "name": "RENCA"
    },

    {
        "name": "CERRO NAVIA"
    },

    {
        "name": "LO PRADO"
    },

    {
        "name": "QUINTA NORMAL"
    },

    {
        "name": "ESTACION CENTRAL"
    },

    {
        "name": "MAIPU"
    },

    {
        "name": "CERRILLOS"
    },

    {
        "name": "LO ESPEJO"
    },

    {
        "name": "EL BOSQUE"
    },

    {
        "name": "SAN BERNARDO"
    },

    {
        "name": "LA PINTANA"
    },

    {
        "name": "LA CISTERNA"
    },

    {
        "name": "PEDRO AGUIRRE CERDA"
    },

    {
        "name": "SAN MIGUEL"
    },

    {
        "name": "SAN JOAQUIN"
    },

    {
        "name": "SAN RAMON"
    },

    {
        "name": "LA GRANJA"
    },

    {
        "name": "PUENTE ALTO"
    },

    {
        "name": "LA FLORIDA"
    },

    {
        "name": "MACUL"
    },

    {
        "name": "NUNOA"
    },

    {
        "name": "PENALOLEN"
    },

    {
        "name": "LA REINA"
    },

    {
        "name": "LAS CONDES"
    },

    {
        "name": "VITACURA"
    },

    {
        "name": "PROVIDENCIA"
    },

    {
        "name": "LO BARNECHEA"
    },

    {
        "name": "RECOLETA"
    },

    {
        "name": "HUECHURABA"
    },

    {
        "name": "INDEPENDENCIA"
    },

    {
        "name": "LAMPA"
    },

    {
        "name": "TALAGANTE"
    },

    {
        "name": "CHICUREO"
    },

    {
        "name": "BUIN"
    },

    {
        "name": "PENAFLOR"
    },

    {
        "name": "PIRQUE"
    },

    {
        "name": "CALERA DE TANGO"
    },

    {
        "name": "PAINE"
    },

    {
        "name": "SAN JOSE DE MAIPO"
    },

    {
        "name": "PLAYA ANCHA"
    }

]


class ValidaComuna():
    def __init__(self, obj, arg, tipo_pago):
        self.json_ = obj
        self.arg_ = arg
        self.tipo_pago_ = tipo_pago

    def logica_validations(self):
        # print("self.json_->", self.json_)
        # print("self.arg_->", self.arg_)
        # n2 = "saNtiaop"
        numero = 0
        comuna = ''

        def search(name, people):
            return [element for element in people if element['id'] == name]

        for comunas in lista_comunas:
            valor = fuzz.ratio(comunas['name'].lower(), self.json_['billing']['city'].lower())
            if valor > numero:
                numero = valor
                comuna = comunas['name']
            if self.json_['id'] in self.arg_:
                self.json_['enviado'] = True
                self.json_['tipodepago'] = search(self.json_['id'], self.tipo_pago_)[0]['tipo']
            else:
                self.json_['enviado'] = False
                self.json_['tipodepago'] = ''

        # print(numero)
        # print(comuna)
        self.json_['billing']['city_ori'] = self.json_['billing']['city']
        self.json_['billing']['porcentaje'] = numero
        self.json_['billing']['city'] = comuna
        return self.json_
