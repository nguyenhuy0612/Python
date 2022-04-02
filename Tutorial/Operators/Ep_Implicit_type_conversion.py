
# ? Implicit type conversion

"""
? a = input("Enter a number: ")
? b = a+2
? print(b)
* Display TypeError: can only concatenate str (not "int") to str
    *เราจะกรองข้อมูลตัวเลข แต่ข้อมูลที่ป้อนเข้ามาผ่านฟังก์ชัน input() จะเป็นข้อมูลชนิดสตริงเสมอ 
"""
# * คือ Python interpreter  จะแปลงชนิดของข้อมูลให้อยู่ในรูปแบบที่เหมาะสมโดยอัตโนมัติ ซึ่ง
# * กฏการแปลงชนิดข้อมูล คือ ชนิดของข้อมูลที่มีความละเอียดของข้อมูลต่ำกว่าจะถูกแปลงไปเป็นชนิดข้อมูล
# * ที่มีความละเอียดของข้อมูลสูงกว่าเสมอ

print("การหาพื้นพี่สีเหลี่ยมผืนผ้า")
width = input("กรุณาป้อนความกว้างของสีเหลี่ยมผืนผ้า: ")
length = input("กรุณาป้อนความยาวของสีเหลี่ยมผืนผ้า: ")
area = int(width) * int(length)
print("พื้นที่สีเหลี่ยมผืนผ้าที่คุณป้อนคือ: ", area)
print("\n")
"""
    * Explicit type conversion คือการ int(width) และ int(length) แปลงค่า
    * ข้อมูลจากสตริงเป็นเลขจำนวณจริง จากนั้นจึงนำค่าความกว้างและยาวมาคูณกัน
"""
cake_price = 85
cookie_price = 15
total_price = cake_price + cookie_price
print("เค้กราคา" + str(cake_price) + "บาท")
print("คุกกี้ราคา" + str(cookie_price) + "บาท")
print("ราคารวม" + str(total_price) + "บาท")
"""
    * Explicit type conversion คือ str(cake_price), str(cookie_price), str(total_price)
    * แปลงค่าข้อมูลจากเลขจำนวณเต็มไปเป็นสจริง ที่ต้องแปลงเป็นสตริงก่อนเพราะ
    * เราจะนำราคานี้มาบวกกับข้อความสตริง เช่น เค้กราคา บาท ถ้าไมแปลงเป็นสตริงจะเกิด ข้อผิดพลาด
"""
