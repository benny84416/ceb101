import shutil
import os
from os import walk
from os.path import join

# database = './images3' # 當下目錄
# keyword = '002' # input('請輸入檔案關鍵字:')
# print(walk(folder))
# class file_copy_move():
#   def __init__(self, database):
#     self.database = database
def file_copy(database):
  for dir1, dir2, imgs in walk(database):
    # print(dir1)
    # print(dir2)
    # print(imgs)
    for i in imgs:
      # print(type(i))
      fullpath = join(dir1,i) # 獲取檔案完整路徑
      # print(fullpath)
      filename = join(i) # 獲取檔案名稱
      # print(filename)
      keyword = filename.split('_')[0] # 獲取類別
      # print(keyword)
      if keyword in filename:
        # if  os.path.exists(database + '/' + filename):
        if not os.path.exists(keyword):
          os.mkdir(keyword)
        if not os.path.exists(keyword + '/' + filename):
          # shutil.move(fullpath, './' + keyword)  # 移動檔到目標資料夾
          shutil.copy(fullpath, './' + keyword) # 複製檔到目標資料夾
          print(filename, '複製到', keyword, '資料夾')
        else:
          print(filename, '已存在，不執行動作')
          pass

# if __name__=="__main__":

database ='./images3'
# print(database)
print(file_copy(database))