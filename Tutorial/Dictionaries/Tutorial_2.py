a = {"A": "Ant", "B": "Bird", "C": "Cat"}
b = {"A": "Aunt", "B": "Boy"}
c = {"A": 1, "D": 4}

a |= b
print(a)
print(b)
a |= c
print(a)
print(c)


# * คำสั่ง a|=b มีความหมายเท่ากับ a = a|b กล่าวคือ จะนำค่าของดิกชันนารี a และ b มา Merge
# * รวมกันและ Update ผลลัพธ์จากการ  Merge กลับเข้าไปยังดิกชันนารี a
