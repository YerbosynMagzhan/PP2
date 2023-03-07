import re
text = str(input())
print(re.findall('[A-Z][^A-Z]*', text))