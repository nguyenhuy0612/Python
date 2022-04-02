a = {"A": "Ant", "B": "Bee", "C": "Cat"}
b = {"A": "Apple", "B": "Banana", "C": "Coconut"}
c = {"A": 1, "D": 4, "E": 5}

x = a | b
print("----------------------------------------------")
print("a = ", a)
print("b = ", b)
print("A|B after", x)
print("----------------------------------------------")
y = a | c
print("a = ", a)
print("c = ", c)
print("A|C after", y)
z = a | b | c
print("----------------------------------------------")
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("A|B|C after", z)
print("----------------------------------------------")
