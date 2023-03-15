import os
p = '/Users/amirkhamraev/pp2(1)/pp2-22B030460/tsis6/dic-and-files/delete.txt'
if os.path.exists(p):
    os.remove(p)
else:
    print('file doesnt exist')