import pymongo
myclient = pymongo.MongoClient("mongodb://95.111.235.214:32773")
# myclient = pymongo.MongoClient("mongodb://95.111.235.214:32768")

# myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/cuiappte"

mydb = myclient["woocomerce"]
mycol = mydb["envios_rapunzel"]


mydbnew = myclient["envios"]
mycolnew = mydbnew["envios_express"]


mytexdev = myclient["tuenvioexpress"]
mytexdevcomunas = mytexdev["comunas"]



# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")