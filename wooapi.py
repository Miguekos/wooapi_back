from woocommerce import API
import json

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_2956dcbaab2fafcffaf2c57134fea7bef119fe96",
#     consumer_secret="cs_446466432ccda985ceafa968b4eb59c19ad08c4c",
#     version="wc/v3"
# )


wcapi = API(
    url="https://prueba.apps.com.pe",
    consumer_key="ck_4bee3dbc20833081d3efb1c9a2fe9d579951e693",
    consumer_secret="cs_9adf07d839c3e9e79a7b09df5b9fb4a42cd8a9b7",
    version="wc/v3"
)

# r = wcapi.get("products").json()
# # r = wcapi.get("orders")
# # asd = json.loads(r.text)
# # print(type(asd))
# print(r)
# print(type(r))
# # print(r.status_code)
# # print(r.text)