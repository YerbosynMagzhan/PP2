def rev(string):
    s = string.split()[::-1]
    s1 = []
    for i in s:
        s1.append(i)
    return " ".join(s1)
String = str(input())
print(rev(String))