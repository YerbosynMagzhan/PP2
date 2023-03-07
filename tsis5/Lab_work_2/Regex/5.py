import re
def t_m(txt):
        patterns = 'a.*?b$'
        if re.search(patterns,  txt):
                return 'Found a match!'
        else:
                return('Not matched!')
            
print(t_m(str(input())))