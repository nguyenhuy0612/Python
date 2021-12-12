for i in range (2,6):
    for x in range(1,13):
        n = i*x
        print("%d x %d = %d"%(i,x,n)) 

number = int(input("ต้องการสูตรคูณแม่ไหน? :"))
for i in range(1,13):
    result = number*i
    print("%d x %d = %d"%(number,i,result))