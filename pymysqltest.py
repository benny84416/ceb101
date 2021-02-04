#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'junxi'
import pymysql
# 建立連線
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='qazwsx698',
                       db='my_db',
                       charset='utf8')
# 建立遊標, 查詢資料預設為元組型別
cursor = conn.cursor()
sql = "show databases"
cursor.execute(sql)
# 獲取第一行資料
# row_1 = cursor.fetchone()
# print(row_1)
# 獲取前n行資料
# row_n = cursor.fetchmany()
# print(row_n)
# 獲取所有資料
row_3 = cursor.fetchall()
print(row_3)
# 提交，不然無法儲存新建或者修改的資料

conn.commit()
# 關閉遊標
cursor.close()
# 關閉連線
conn.close()