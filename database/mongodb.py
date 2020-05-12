import pymongo
myclient = pymongo.MongoClient("mongodb://95.111.235.214:32773")

mydb = myclient["woocomerce"]
mycol = mydb["envios_olva"]

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")