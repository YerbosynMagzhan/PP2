s = str(input())
first = s[s.find(' ') + 1:]
second = s[:s.find(' ')]
print(first + ' ' + second)