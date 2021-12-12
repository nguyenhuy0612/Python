
i = input("กรุณาใส่คะแนนของคุณ")

if(int(i) >= 0 and int(i) <=40):
    print("เกรด F")
    print("ไปเรียนใหม่ไอโง่")

print("-----------------------")
if(int(i) >= 0 and int(i) <=40):
    print("เกรด F")
elif(int(i) >= 41 and int(i) <=50): 
    print("เกรด D")  
elif(int(i) >= 51 and int(i) <=60):   
    print("เกรด C")   
elif(int(i) >= 61 and int(i) <=70):     
    print("เกรด B")
elif(int(i) >= 71 and int(i) <=80): 
    print("เกรด A")
print("-----------------------")
   