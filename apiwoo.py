from woocommerce import API
import json

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_2956dcbaab2fafcffaf2c57134fea7bef119fe96",
#     consumer_secret="cs_446466432ccda985ceafa968b4eb59c19ad08c4c",
#     version="wc/v3"
# )


wcapi = API(
    url="https://www.rapunzelorganic.cl",
    consumer_key="ck_712386a01acf9c4410b9bab7c29c714a93ac0986",
    consumer_secret="cs_b1345222af870f72a9c0cdc7f0f94cafdb8e6cbb",
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