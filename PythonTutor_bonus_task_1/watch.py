n = int(input())
hours = n // 60
minutes = n - (hours * 60)
division = hours // 24
if hours >= 24:
    hours -= 24 * division
if minutes == 60:
    hours += 1
print(hours, minutes)