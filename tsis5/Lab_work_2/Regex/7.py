import re
txt=str(input())
ans=""
res=re.split(r"[_]",txt)
for i in res:
    ans+=i.capitalize()
print(ans)