jsonR = {
    "meta_data": [
        {
            "id": 1089819,
            "key": "is_vat_exempt",
            "value": "no"
        },
        {
            "id": 1089820,
            "key": "departamento",
            "value": "Lima"
        },
        {
            "id": 1089821,
            "key": "provincia",
            "value": "Lima"
        },
        {
            "id": 1089822,
            "key": "distrito",
            "value": "Lima"
        },
        {
            "id": 1089823,
            "key": "_wc_facebook_for_woocommerce_order_placed",
            "value": "yes"
        },
        {
            "id": 1089872,
            "key": "_ga_tracked",
            "value": "1"
        },
        {
            "id": 1089958,
            "key": "_wc_shipment_tracking_items",
            "value": [
                {
                    "date_shipped": "1600128000",
                    "tracking_id": "a51b6661efac402935259a80011cb864",
                    "tracking_number": "111222",
                    "tracking_product_code": "",
                    "tracking_provider": "dhl-at"
                }
            ]
        }
    ]
}


# for asd in jsonR['meta_data']:
#     if (asd['key'] == "_wc_shipment_tracking_items"):
#         asd['value'][0]['tracking_number'] = "qweqwe"
#         print(asd['value'][0]['tracking_number'])

# print(jsonR)
print(jsonR['meta_data'][6]['value'][0]['tracking_number'])
