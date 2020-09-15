from woocommerce import API
import json

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_2956dcbaab2fafcffaf2c57134fea7bef119fe96",
#     consumer_secret="cs_446466432ccda985ceafa968b4eb59c19ad08c4c",
#     version="wc/v3"
# )


#wcapi = API(
#    url="https://euphoria.pe",
#    consumer_key="ck_24372cd19576ca2dacd27540ce4d88f391d2f9dd",
#    consumer_secret="cs_ac4f95f51cc9db55cf7cdb78a7facb0f82bb4329",
#    version="wc/v3",
#    timeout=20
#)

wcapi = API(
    url="https://euphoria.pe",
    consumer_key="ck_d7ac347b00f28c31c0e8b001759d34d59d4c6e9f",
    consumer_secret="cs_9c74368749e724a18cd8dc1b06b7275781765eb6",
    version="wc/v3",
    timeout=20
)

# asd = wcapi.get("products", params={"per_page": 100}).json()
# print(asd)
# print(len(asd))

# r = wcapi.get("products/24965").json()
# r = wcapi.get("orders").json()
# r = wcapi.get("orders")
# asd = json.loads(r.text)
# print(type(asd))
# print(r)
# print(len(r))
# print(type(r))
# print(r.status_code)
# print(r.text)
