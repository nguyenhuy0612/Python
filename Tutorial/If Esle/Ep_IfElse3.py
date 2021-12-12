
w = 1

while w < 6:
    passl = input("กรุณาใส่รหัส :")

    if passl == "1234":
        print("รหัสถูกต้อง :")
        fruits = ["Apple","Banana","Cherry"]
        for x in fruits:
            print(x)
            break
    else:
        print("รหัสไม่ถูกต้อง :")
    
    w += 1
else:
    print("รหัสห้ามผิดเกิน 4 ครั้ง :")    











