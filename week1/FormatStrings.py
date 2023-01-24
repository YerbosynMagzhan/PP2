#ERROR

# age = 33
# text = "My name is Kiro Yoshikage, I am" + age
# print(text)


age = 33
text = "My name is Kiro Yoshikage, I am {}"
print(text.format(age))

age = 33
hometime = 8
sleeptime = 11
bio = "My name is Yoshikage Kira. I'm {} years old. I get home every day by {} PM at the latest. I'm in bed by {} PM"
print(bio.format(age, hometime, sleeptime))

age = 33
hometime = 8
sleeptime = 11
bio = "My name is Yoshikage Kira. I'm {2} years old. I get home every day by {0} PM at the latest. I'm in bed by {1} PM"
print(bio.format(age, hometime, sleeptime))