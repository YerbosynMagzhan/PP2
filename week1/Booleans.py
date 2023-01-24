# print(44>21)
# print(10==4)
# print(444<555)

a = 333
b = 123

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

print(bool("Hello"))
print(bool(15)) 


x = "Hello"
y = 15
print(bool(x))
print(bool(y))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


'''
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class 
with a __len__ function that returns 0 or False
'''
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))



def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#check if an object is an integer or not
x = 200
print(isinstance(x, int))