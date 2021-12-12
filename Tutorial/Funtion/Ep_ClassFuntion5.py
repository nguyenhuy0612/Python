class student:
    def __init__(self, sid, name, tel, bdate):
        self.sid = sid
        self.name = name
        self.tel = tel
        self.bdate = bdate
        
    def getDetail(self):
        print('รัหส: %s' % self.sid)
        print('ชื่อ-นามสกุล: %s' % self.name)
        print('เบอร์โทร: %s' % self.tel)
        if(int(i) >= 0 and int(i) <=40):
            print("เกรด F")
        elif(int(i) >= 41 and int(i) <=50): 
            print("เกรด D")
        elif(int(i) >= 51 and int(i) <=60):   
            print("เกรด C")   
        elif(int(i) >= 61 and int(i) <=70):     
            print("เกรด B")
        elif(int(i) >= 71 and int(i) <=80): 
            print("เกรด A")



    def howold(self):
        old = 2564 - float(self.bdate)  
        print('อายุ: %d' % old)
        
class subject:
    def __init__(self,subjid,subjname):
        self.subjid = subjid
        self.subjname = subjname

    def show(self):
        print('รหัสวิชา %s' %self.subjid)
        print('ชื่อวิชา %s' % self.subjname)

    

sub1 = subject('E0101','เขียนโปรแกรม')
sub2 = subject('E0102','คณิต')
sub3 = subject('E0103','ภาษาอังกฤษ')
sub4 = subject('E0104','ว่ายน้ำ')

b1 = student(1,1,1,1)

b1.sid = input("รหัส:")
b1.name = input("ชื่อ:")
b1.tel = input("เบอร์โทร:")
p = input("ปีเกิด:")
b1.bdate = int(p)
s1 = input("เลือกวิชาที่ลง E0101,E0102,E0103,E0104 :")
i = input("กรุณใส่คะแนน")
print("-----------------------")
b1.getDetail()
b1.howold()
if s1 == 'E0101':
    sub1.show()
elif s1 == 'E0102':
    sub2.show()
elif s1 == 'E0103':
    sub3.show()
elif s1 == 'E0104':
    sub4.show()
else:
    print("เลือกวิชาไม่ถูก")   
print("-----------------------")



