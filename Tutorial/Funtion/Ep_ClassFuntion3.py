
class skill:
    skill = []

class ability:
    att = None
    arm = None
    deF = None
    hp1  = None
    mana = None

    def get_ability(self,at,ar,de,hp,ma):
        self.att = at
        self.arm = ar
        self.deF = de
        self.hp1 = hp
        self.mana = ma

class hero(skill,ability):
    name = None
    St   = None
    agi  = None
    Int  = None
    Type = None

    def get_data(self,a,b,c,d,e):
        self.name = a
        self.St   = b
        self.agi  = c
        self.Int  = d
        self.Type = e

ch = hero();
print("ข้อมูล ตัวละครของคุณ")

n = input("ชื่อตัวละคร:")
s = input("ความแข็งแกร่ง str:")
a = input("ค่าความว่องไว agi:")
i = input("ค่าสติปัญญา  int:")
t = input("ประเภท Hero:")

at = input("ค่าโจมตี")
ar = input("ค่าเกราะ")
de = input("ค่าป้องกัน:")
hp = input("พลังชีวิต")
ma = input("มานา")

ch.get_data(n,s,a,i,t)
ch.get_ability(at,ar,de,hp,ma)

print("ตั้งค่าสกิล")
i = input("จำนวนของ สกิล ที่ต้องการ:")

j = 1
while j <= int(i):
    sk = input("สกิล:")
    ch.skill.append(sk)
    j = j+1

print("---ข้อมูลตัวละคร---")
print("ชื่อตัวละคร :",ch.name)
print("ค่าความแข็งแกร่ง :",ch.St)
print("ค่าความว่องไว :",ch.agi)
print("ค่าสติปัญญา :",ch.Int)
print("Class ตัวละคร:",ch.Type)
print("----------------")

 