class skills:
    
    skill = []

class ability:
    att_ = None
    arm_ = None
    def_ = None
    hp_ = None
    mana_ = None

    def get_ability(self,at,ar,de,hp,ma):
        self.att_ = at
        self.arm_ = ar
        self.def_ = de
        self.hp_ = hp
        self.mana_ = ma


class hero(skills,ability):
    name = None
    str_ = None
    agi_ = None
    int_ = None
    type_ = None

    def get_data(self,a,b,c,d,e):
        self.name = a
        self.str_ = b
        self.agi_ = c
        self.int_ = d
        self.type_ = e


Character = hero();
print("ตั้งค่าข้อมูล Hero")
n = input("ชื่อ Hero:")
s = input("ค่าความแข็งแกร่ง str:")
a = input("ค่าความว่องไว agi:")
i = input("ค่าสติปัญญา int:")
t = input("ประเภท Hero:")

at = input("ค่าโจมตี:")
ar = input("ค่าเกราะ:")
df = input("ค่าป้องกันเวท:")
hp = input("พลังชีวิต:")
ma = input("Mana:")

Character.get_data(n,s,a,i,t)
Character.get_ability(at,ar,df,hp,ma)

print("------------------------------")
print("ตั้งค่า skill")
i = input("จำนวนของ Skill ที่ต้องการ:")

j = 1

while j <= int(i):
    ss = input("Skill:")
    Character.skill.append(ss)
    j = j+1

print("--------- My Hero ------------")
print("ชื่อ Hero ",Character.name)
print("ค่าความแข็งแกร่ง ",Character.str_)
print("ค่าความว่องไว ",Character.agi_)
print("ค่าสติปัญญา ",Character.int_)
print("ประเภท Hero ",Character.type_)
print("------------------------------")
print("พลังโจมตี ",Character.att_)
print("เกราะ ",Character.arm_)
print("ป้องกันเวท ",Character.def_)
print("พลังชีวิต ",Character.hp_)
print("มานา ",Character.mana_)
print("------------------------------")
print("ข้อมูล Skills")
print(Character.skill)
print("------------------------------")

j = 1

while j < 2:
    at = input("โจมตี Here:")
    dammage = int(at) - int(Character.arm_)

    if int(dammage) < 0:
        dam = 0
    else:
        dam = dammage

    Character.hp_ = int(Character.hp_) - int(dam)

    if int(Character.hp_) < 0:
        print("Hero ตาย")
        break
    else:
        print("พลังชีวิตเหลือ",Character.hp_)
        print("สู้ได้ต่อ")
        
