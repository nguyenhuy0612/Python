v = 0
u = 0
x = 0
sentence = '7330XF04327DG0V5HSIIWV0GBE6NX2'

for a in sentence:
    if a in "1234567890":
        v = v+1
    if  a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        u = u+1
print ("จำนวณตัวเลข :",(v)) 
print ("จำนวณอักษร :",(u))              

data = [97,76,13,99,84,93,65,69,32,77,18,74,11,37,96,39,6,32,69,48]    
number = []

for i in data:
    if (x%2):
        number.append('odd')
    else:
        number.append('even')
print("data : ",data)
print("number : ",number)
 