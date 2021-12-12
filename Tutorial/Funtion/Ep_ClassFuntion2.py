
class character:
    def __init__(self):
        self.name = ""
        self.skill = ""
        self.level = ""     
#-----------------------
c1 = character()
c1.name = "Highwayman"
c1.skill = "ตีไกล"
c1.level = "Level 5"
#-----------------------
c2 = character()
c2.name = "Antiquarian"
c2.skill = "ใช้พิษ"
c2.level = "Level 3"
#-----------------------
c3 = character()
c3.name = "Grave Robber"
c3.skill = "เจาะเกราะได้"
c3.level = "Level 4"
#-----------------------
print("ตัวละคร:",c1.name,c1.skill,c1.level)
print("ตัวละคร:",c2.name,c2.skill,c2.level)
print("ตัวละคร:",c3.name,c3.skill,c3.level)

