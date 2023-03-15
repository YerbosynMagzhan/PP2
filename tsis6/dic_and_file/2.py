import os
print('existance: ',os.access('/Users/amirkhamraev/pp2(1)/pp2-22B030460', os.F_OK))
print('readability: ', os.access('/Users/amirkhamraev/pp2(1)/pp2-22B030460', os.R_OK))
print('writability: ', os.access('/Users/amirkhamraev/pp2(1)/pp2-22B030460/', os.W_OK))
print('executability: ', os.access('/Users/amirkhamraev/pp2(1)/pp2-22B030460/', os.X_OK))