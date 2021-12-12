
class student:
    def __init__(self,name,lname,studentcode,phonenumber,year):
        self.name = name
        self.lname = lname
        self.studentcode = studentcode
        self.phonenumber = phonenumber
        self.year = year
        
    def Full(self):
        print('ชื่อ: %s' % self.name)
        print('นามสกุล: %s ' % self.lname)
        print('รหัสนิสิต: %s' % self.studentcode)   
        print('เบอร์: %s' % self.phonenumber)
        self.year = 2021 - int(self.year)
        print('อายุ: %d' % self.year)        

     


n1 = student (1,1,1,1,1)

n1.name  = input ("ชื่อ :")
n1.lname = input("นามสกุล :")
n1.studentcode = input("รหัสนิสิต :")
n1.phonenumber = input("เบอร์โทร :")
n1.year = input ("ปีเกิด :")
n1.Full()


