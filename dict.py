import sys


sys.argv = sys.argv[1::]
arg = {}
flag = False
for i in sys.argv:
    if i == '--sort':
        flag = True
        continue
    temp = f'Key: {i.split("=")[0]} Value:'
    arg[temp] = i.split('=')[1]
if flag:
    for i, j in sorted(arg.items()):
        print(i, j)
else:
    for i, j in arg.items():
        print(i, j)
