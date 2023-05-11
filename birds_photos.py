import os
count=0
a=os.walk(top="F:\\鸟种记录照片")
b=os.walk(top="E:\\animals\\鸟种记录照片")
print("有照片记录的物种：")
for i,j in zip(a,b):
    if i[2]!=[]:#有记录照片的
        count+=1        
        print(i[0])