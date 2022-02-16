# jsonR = {
#     "meta_data": [
#         {
#             "id": 1089819,
#             "key": "is_vat_exempt",
#             "value": "no"
#         },
#         {
#             "id": 1089820,
#             "key": "departamento",
#             "value": "Lima"
#         },
#         {
#             "id": 1089821,
#             "key": "provincia",
#             "value": "Lima"
#         },
#         {
#             "id": 1089822,
#             "key": "distrito",
#             "value": "Lima"
#         },
#         {
#             "id": 1089823,
#             "key": "_wc_facebook_for_woocommerce_order_placed",
#             "value": "yes"
#         },
#         {
#             "id": 1089872,
#             "key": "_ga_tracked",
#             "value": "1"
#         },
#         {
#             "id": 1089958,
#             "key": "_wc_shipment_tracking_items",
#             "value": [
#                 {
#                     "date_shipped": "1600128000",
#                     "tracking_id": "a51b6661efac402935259a80011cb864",
#                     "tracking_number": "111222",
#                     "tracking_product_code": "",
#                     "tracking_provider": "dhl-at"
#                 }
#             ]
#         }
#     ]
# }
#
#
# # for asd in jsonR['meta_data']:
# #     if (asd['key'] == "_wc_shipment_tracking_items"):
# #         asd['value'][0]['tracking_number'] = "qweqwe"
# #         print(asd['value'][0]['tracking_number'])
#
# # print(jsonR)
# print(jsonR['meta_data'][6]['value'][0]['tracking_number'])


from fuzzywuzzy import fuzz

# n1= "Saniano"
# n2 = "santiago"
#
# print(fuzz.partial_ratio(n1.lower(), n2.lower()))


"""
lista_comunas = [
    {
        "name": "SANTI"
    },
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
"""
#
#
"""
class ValidaComuna():
    def __init__(self, obj):
        self.json_ = obj

    def logica_validations(self):
        # print("self.json_->", self.json_)
        n2 = "saNtiaop"
        numero = 0
        comuna = ''
        for comunas in lista_comunas:
            valor = fuzz.ratio(comunas['name'].lower(), n2.lower())
            if valor > numero:
                numero = valor
                comuna = comunas['name']
        # print(numero)
        # print(comuna)
        self.json_['billing']['city'] = comuna
        return  self.json_
"""
"""
json_test = [
    {
        "_links": {
            "collection": [
                {
                    "href": "https://www.rapunzelorganic.cl/wp-json/wc/v3/orders"
                }
            ],
            "self": [
                {
                    "href": "https://www.rapunzelorganic.cl/wp-json/wc/v3/orders/19865"
                }
            ]
        },
        "billing": {
            "address_1": "Villa Balmaceda Calle A nro 933",
            "address_2": "",
            # "city": "Curic\u00f3",
            "city": "SANTIAGO",
            "company": "",
            "country": "CL",
            "email": "",
            "first_name": "Karen Angelica",
            "last_name": "arrasco Lucero",
            "phone": "998744566",
            "postcode": "",
            "state": ""
        },
        "cart_hash": "",
        "cart_tax": "0",
        "coupon_lines": [],
        "created_via": "admin",
        "currency": "CLP",
        "currency_symbol": "$",
        "customer_id": 0,
        "customer_ip_address": "",
        "customer_note": "",
        "customer_user_agent": "",
        "date_completed": None,
        "date_completed_gmt": None,
        "date_created": "2022-02-09T13:27:05",
        "date_created_gmt": "2022-02-09T16:27:05",
        "date_modified": "2022-02-09T14:07:34",
        "date_modified_gmt": "2022-02-09T17:07:34",
        "date_paid": "2022-02-09T14:07:34",
        "date_paid_gmt": "2022-02-09T17:07:34",
        "discount_tax": "0",
        "discount_total": "0",
        "fee_lines": [],
        "id": 19865,
        "line_items": [
            {
                "id": 26595,
                "meta_data": [
                    {
                        "display_key": "_reduced_stock",
                        "display_value": "1",
                        "id": 253981,
                        "key": "_reduced_stock",
                        "value": "1"
                    }
                ],
                "name": "kit completo de crecimiento y anti caida",
                "parent_name": None,
                "price": 35990,
                "product_id": 871,
                "quantity": 1,
                "sku": "",
                "subtotal": "35990",
                "subtotal_tax": "0",
                "tax_class": "",
                "taxes": [],
                "total": "35990",
                "total_tax": "0",
                "variation_id": 0
            }
        ],
        "meta_data": [
            {
                "id": 653205,
                "key": "_new_order_email_sent",
                "value": "true"
            }
        ],
        "number": "19865",
        "order_key": "wc_order_Lm0UodGM4CK3s",
        "parent_id": 0,
        "payment_method": "other",
        "payment_method_title": "other",
        "prices_include_tax": False,
        "refunds": [],
        "shipping": {
            "address_1": "",
            "address_2": "",
            "city": "",
            "company": "",
            "country": "",
            "first_name": "",
            "last_name": "",
            "postcode": "",
            "state": ""
        },
        "shipping_lines": [],
        "shipping_tax": "0",
        "shipping_total": "0",
        "status": "processing",
        "tax_lines": [],
        "total": "35990",
        "total_tax": "0",
        "transaction_id": "",
        "version": "5.0.0"
    },
    {
        "_links": {
            "collection": [
                {
                    "href": "https://www.rapunzelorganic.cl/wp-json/wc/v3/orders"
                }
            ],
            "self": [
                {
                    "href": "https://www.rapunzelorganic.cl/wp-json/wc/v3/orders/19864"
                }
            ]
        },
        "billing": {
            "address_1": "Lincoyan 1132",
            "address_2": "",
            "city": "linachi",
            "company": "",
            "country": "",
            "email": "leckie.tamara@gmail.com",
            "first_name": "Tamara",
            "last_name": "Leckie",
            "phone": "9 4131 0001",
            "postcode": "",
            "state": "RM"
        },
        "cart_hash": "df32e2f677a945e580e7d047c39f90c2",
        "cart_tax": "0",
        "coupon_lines": [],
        "created_via": "checkout",
        "currency": "CLP",
        "currency_symbol": "$",
        "customer_id": 0,
        "customer_ip_address": "181.43.131.84",
        "customer_note": "",
        "customer_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 220.0.0.8.117 (iPhone13,2; iOS 14_7_1; es_PE; es-PE; scale=3.00; 1170x2532; 347566818) NW/3",
        "date_completed": None,
        "date_completed_gmt": None,
        "date_created": "2022-02-09T13:26:26",
        "date_created_gmt": "2022-02-09T16:26:26",
        "date_modified": "2022-02-09T13:28:29",
        "date_modified_gmt": "2022-02-09T16:28:29",
        "date_paid": "2022-02-09T13:28:29",
        "date_paid_gmt": "2022-02-09T16:28:29",
        "discount_tax": "0",
        "discount_total": "0",
        "fee_lines": [],
        "id": 19864,
        "line_items": [
            {
                "id": 26590,
                "meta_data": [
                    {
                        "display_key": "_reduced_stock",
                        "display_value": "1",
                        "id": 253942,
                        "key": "_reduced_stock",
                        "value": "1"
                    }
                ],
                "name": "kit completo de crecimiento y anti caida",
                "parent_name": None,
                "price": 35990,
                "product_id": 871,
                "quantity": 1,
                "sku": "",
                "subtotal": "35990",
                "subtotal_tax": "0",
                "tax_class": "",
                "taxes": [],
                "total": "35990",
                "total_tax": "0",
                "variation_id": 0
            }
        ],
        "meta_data": [
            {
                "id": 653077,
                "key": "is_vat_exempt",
                "value": "no"
            },
            {
                "id": 653078,
                "key": "rut",
                "value": "182465674"
            },
            {
                "id": 653131,
                "key": "_new_order_email_sent",
                "value": "true"
            }
        ],
        "number": "19864",
        "order_key": "wc_order_eXKWSrAEOAYM2",
        "parent_id": 0,
        "payment_method": "flow_webpay",
        "payment_method_title": "Webpay",
        "prices_include_tax": False,
        "refunds": [],
        "shipping": {
            "address_1": "",
            "address_2": "",
            "city": "",
            "company": "",
            "country": "",
            "first_name": "",
            "last_name": "",
            "postcode": "",
            "state": ""
        },
        "shipping_lines": [],
        "shipping_tax": "0",
        "shipping_total": "0",
        "status": "processing",
        "tax_lines": [],
        "total": "35990",
        "total_tax": "0",
        "transaction_id": "",
        "version": "5.0.0"
    }
]

"""
# new_json_response = []
# #
# for pedidos in json_test:
#     validar = ValidaComuna(pedidos)
#     # print(validar.logica_validations())
#     new_json_response.append(validar.logica_validations())
#
#
# print("new_json_response->", new_json_response)

# print(fuzz.ratio(n1.lower(), n2.lower()))
# print(fuzz.partial_ratio(n1.lower(), n2.lower()))
# print(fuzz.token_sort_ratio(n1.lower(), n2.lower()))

# dicts = [
#     {
#         'name': 'Juan',
#         'id': 'Pagado'
#     },
#     {
#         'name': 'Pedro',
#         'id': 'Por Pagar'
#     }
# ]
#
# values = [d['name'] for d in dicts if 'name' == '']
# print(values)
#
# people = [
#     {'name': "Tom", 'age': 10},
#     {'name': "Mark", 'age': 5},
#     {'name': "Pam", 'age': 7}
# ]
#
#
# def search(name, people):
#     return [element for element in people if element['name'] == name]
#
#
# print(search('Tom', people))


# ini: 20409
# fin: 30000
n1 = 20409
n2 = 30000

asd = n1

while n1 < n2:
    print(n1 + 1)
    asd = "{},{}".format(asd, n1 + 1)
    # print(asd)
    n1 = n1 + 1

print(asd)