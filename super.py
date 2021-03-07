import sys


n = 0
lst = []
count = False
num = False
sort = False
sys.argv = sys.argv[1::]
for i in sys.argv:
    if i == '--count':
        count = True
        continue
    if i == '--num':
        num = True
        continue
    if i == '--sort':
        sort = True
        continue
    try:
        f = open(i, 'r')
    except Exception as err:
        print('ERROR')
        exit(0)
for i in f.readlines():
    lst.append(i.rstrip())
if sort and num:
    lst = sorted(lst)
    if count:
        for i in lst:
            print(n, i)
            n += 1
        print('rows count:', n)
        exit(0)
    else:
        for i in lst:
            print(n, i)
            n += 1
        exit(0)
elif sort:
    lst = sorted(lst)
elif num:
    if count:
        for i in lst:
            print(n, i)
            n += 1
        print('rows count:', n)
        exit(0)
    else:
        for i in lst:
            print(n, i)
            n += 1
        exit(0)
if count:
    for i in lst:
        print(i)
    print('rows count:', len(lst))
    exit(0)
else:
    for i in lst:
        print(i)
