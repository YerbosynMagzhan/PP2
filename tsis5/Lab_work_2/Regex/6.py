import re
txt = str(input())
print(re.sub("[ ,.]", ":", txt))