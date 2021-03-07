import sys


n = 0
t = 0
if len(sys.argv) == 1:
    print("NO PARAMS")
    exit(0)
try:
    n = int(sys.argv[1])
    for i in range(len(sys.argv)):
        if len(sys.argv) > 2:
            if t % 2 == 0:
                n = n - int(sys.argv[i + 2])
                t += 1
            else:
                n = n + int(sys.argv[i + 2])
                t += 1
        else:
            print(n)
            exit(0)
except IndexError as err:
    print(n)
except Exception as err:
    print(err.__class__.__name__)
