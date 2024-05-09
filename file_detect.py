import os

str = r"D:\demo.txt"
print(str)

if os.path.exists(str):
    print("路徑檔案存在")
else:
    print("路徑不存在")

if os.path.isfile(str):
    print("是檔案")
else:
    print("不是檔案")
    
