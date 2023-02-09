s = str(input())
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
elif s.count('f') >=2:
    print(s.find('f', s.find('f') + 1))