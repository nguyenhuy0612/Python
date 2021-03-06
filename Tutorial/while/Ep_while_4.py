
# ? การทำงานของคำสั่ง for ร่วมกบฟังก์ชั่น range()

"""
    * เราสามารถนำฟังก์ชัน range() มาใช้กำหนดรอบการทำงานของคำสั่งทำซ้ำ for ได้ เพื่อกำหนด ว่าให้คำสั่ง 
    * for วนซ้ำการทำงานทั้งหมดกี่รอบ ดังรูปแบบต่อไปนี้
        * for ตัวแปร  in range(จำนวนรอบการทำงาน):
        * คำสั่งการทำงาน
            * โดยรอบการทำงานฟังก์ชัน range() จะเริ่มต้นที่ 0 และเพิ่มค่าขึ้นที่ละ 1 ค่า ดังนั้นหาก
            * กำหนด range ให้กับคำสั่งทำซ้ำ for แล้วคำสั่ง for จะวนซ้ำการทำงานทั้งหมดเท่ากับ
            * จำนวนการทำงาน -1 รอบ            
"""

for x in range(5):
    print("รอบที่", x)
    print("*")
