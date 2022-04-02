
# * การลบข้อมูลจากดันชันนารีด้วยฟังก์ชั่น pop() และ del()
# * การลบข้อมูลลงด้วยฟังก์ชั่น pop() ทำได้ดังรูปแบบต่อไปนี้
# * ดิกชันนารีที่ต้องการลบข้อมูล.pop(key)
# * del ดิกชันนารีที่ต้องการลบข้อมูล[key]

# ? แสดงกสนลบข้อมูลในดิกชันนารี

number_dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
}
a = 5
number_dict.pop(3)
print(number_dict)
del number_dict[5]
print(number_dict)
print("\n")
print(type(number_dict))
