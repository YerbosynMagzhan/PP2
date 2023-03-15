import os
p = ('/Users/amirkhamraev/pp2(1)/pp2-22B030460/tsis6/dic-and-files/1.py')
#p = (os.getcwd)
if os.path.exists:
    print("filename and directory portion of the given path: ")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print('path ddoesnt exist')