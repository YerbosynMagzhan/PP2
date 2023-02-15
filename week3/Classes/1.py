class Myclass:
    def __init__(self):
        self.str = None
    def getString(self):
        self.str = str(input())
    def printString(self):
        print(self.str.upper())

string = Myclass()
string.getString()
string.printString()