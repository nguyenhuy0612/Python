class Player:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.number= ""
class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

if __name__ == '__main__':
    p1 = Player()
    p1.fname = "Laser"
    p1.lname = "Online"
    p1.number = 1

    p2 = Player()
    p2.fname = "Alex"
    p2.lname = "Maxger"
    p2.number = 2     

    p3 = Player()
    p3.fname = "Stalin"
    p3.lname = "iron"
    p3.number = 3

