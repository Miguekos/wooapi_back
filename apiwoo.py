from woocommerce import API
import json

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_2956dcbaab2fafcffaf2c57134fea7bef119fe96",
#     consumer_secret="cs_446466432ccda985ceafa968b4eb59c19ad08c4c",
#     version="wc/v3"
# )


wcapi = API(
    url="https://wordpressfive.apps.com.pe",
    consumer_key="ck_82be01f54acaee8b37ed61a161a8fee07f75d4f7",
    consumer_secret="cs_a93ae263eb2abd848b5f0ae8dc96079a1fe5b080",
    version="wc/v3",
    timeout=20
)

# r = wcapi.get("products").json()
# r = wcapi.get("orders").json()
# # asd = json.loads(r.text)
# # print(type(asd))
# print(r)
# print(type(r))
# # print(r.status_code)
# # print(r.text)