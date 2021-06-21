import os
import time
import shutil
path = "C:/Users/admin/Desktop/Coding/Python"
days = 30 
Dtime = 30*24*60*60
sec = Dtime - time.time()
isExist = os.path.exists(path)
print(isExist)
list = os.listdir(path)
print(list)
split = os.walk(path)
print(split)
join = os.path.join(path + "/C-99/1.JPG")
isJoinExist = os.path.exists(join)
print(isJoinExist)
ctime =  os.stat(path).st_ctime
print(ctime)
if(sec > ctime):
     os.remove(join)
elif(isJoinExist == False):
    print ("path not found")