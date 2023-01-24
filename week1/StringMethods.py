text = "Welcome to the ProgrammLand"
x = text.capitalize()
print(x)
#Converts the first character to upper case


text = "Welcome to the ProgrammLand"
x = text.casefold()
print(x)
#Converts string into lower case


text = "Welcome"
x = text.center(20, "#")
print(x)
#Returns a centered string


text = "Welcome to the ProgrammLand, welcome"
x = text.count("welcome")
print(x)
#Returns the number of times a specified value occurs in a string


txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#Returns an encoded version of the string


txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
#Returns true if the string ends with the specified value


txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
#Sets the tab size of the string


txt = "Hello, welcome to my world."
x = txt.find("e", 1, 7)
print(x)
#Searches the string for a specified value and returns the position of where it was found


