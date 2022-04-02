
"""
    ?โปรแกรมแสดงการพิมพ์ค่าข้อมูลในลิสต์ ทูเพิล เซต และดิกชันนารี โดยใช้คำสั่งทำซ้ำ for

"""
mylist = ["apple", "orange"]
mytuple = {"square", "circle"}
myset = {"Chocolate", "Vanilla", "Strawberry"}
mydict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
}

for x in mylist:
    print(x)
for x in mytuple:
    print(x)
for x in myset:
    print(x)
for x in mydict:
    print(x)

"""
    * คำสั่งทำซ้ำ for จะวนซ้ำการทำงานไปเรื่อยๆ เพื่อดึงค่าข้อมูลของลิสต์ ทูเพิล และ เซตมาแสดงทาง
    * หน้าจอจนครบทุกตัว ส่วยชนิดข้อมูลดิกซันนารี คำสั่ง for จะดึงค่าคียมาแสดงผลที่หน้าจอ
"""
