str = input()

low = 0
up = 0

for i in str:
    if i >= 'a' and i <= 'z':
        low+=1
    else:
        up+=1
print(f'low: {low} up: {up}')