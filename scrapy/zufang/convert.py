import pymongo
import pandas as pd
client = pymongo.MongoClient(host="localhost", port=27017)
db = client.zufang6
collection = db.lianjia


total_docs = collection.find({}, {"_id":0})
total_items = []
for x in total_docs:
    items = {i:str(j).strip() for i, j in zip(list(x.keys()), list(x.values()))}
    # print(items)
    total_items.append(items)

xx = pd.DataFrame(total_items)
print(xx)
xx.to_csv("t1.csv", index=False, encoding="gb18030")
