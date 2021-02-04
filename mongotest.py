import pymongo
# import img_similarity2
import os
from gridfs import *

# find_img

myclient = pymongo.MongoClient(
    'localhost',27017
    )
# print(myclient)
# mydb = myclient["test"]
mydb = myclient.test
# print(mydb)
# mycol = mydb["wow8"]
mycol = mydb.tmark_json
# print(mycol)
# results = mycol.find({})
results = mycol.find({})
# results = mycol.find({'price':{'$gt':200}}) #
# results2 = mycol.find({}, sort=[('_id', -1)]).limit(2)
# print(results)
for result in results:
    # print(result)
    try:
        n = "000000015"
        if result["_id"] == n:
            b = result["image"]
            print(b)
    except:
        pass




#
member = {

            'Name': 'peter',
            "item": 'money',
            "size":9999,
            "price": '$$$$$',

            'Name': 'peter',
            "item": 'water',
            "Quantity": 1,
            "price": 120
            }
# myclient = pymongo.MongoClient(
#         "mongodb+srv://eks210017:eks210017@cluster0.yrvuu.mongodb.net/mydatabase?retryWrites=true&w=majority")
# mydb = myclient["mydatabase"]
# mycol.insert_many([member])
# results = mycol.find_one({'Name': 'wawa'})
# print(results)
# test = mycol.delete_many({'Name': 'wawa'})
# print(test.deleted_count)

# 對於數據更新要使用update方法
# condition={'Name': 'wawa'}
# student=mycol.find_one(condition)
# # print(student)
# student['price']=600
# result=mycol.update_one(condition,{'$set':student})
# print(result)

# #本地硬碟上的圖片目錄
# dirs = './images3'
# #列出目錄下的所有圖片
# files = os.listdir(dirs)
# #遍歷圖片目錄集合
# for file in files:
#     #圖片的全路徑
#     filesname = dirs + '/' + file
#     #分割，為了儲存圖片檔案的格式和名稱
#     f = file.split('.')
#     #類似於建立檔案
#     datatmp = open(filesname, 'rb')
#     #建立寫入流
#     imgput = GridFS(mydb)
#     #將資料寫入，檔案型別和名稱通過前面的分割得到
#     insertimg=imgput.put(datatmp,content_type=f[1],filename=f[0])
#     datatmp.close()
# print("js")

# from pymongo ifrom gridfs import *
# myclient = pymongo.MongoClient(
#         "mongodb+srv://eks210017:eks210017@cluster0.yrvuu.mongodb.net/mydatabase?retryWrites=true&w=majority")
# mydb = myclient["mydatabase"]
# #给予girdfs模块来写出，其中collection为上一步生成的，我不知道怎么该名称。实际上是由fs.flies和fs.chunks组成
# gridFS = GridFS(mydb, collection="fs")
# count=0
# for grid_out in gridFS.find():
#     count+=1
#     print(count)
#     data = grid_out.read() # 获取图片数据
#     outf = open('%s.jpg' % count,'wb')#创建文件
#     outf.write(data)  # 存储图片
#     outf.close()mport MongoClient
#