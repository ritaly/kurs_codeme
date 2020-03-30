import os

path = 'poem.txt'
if os.path.exists(path) and os.stat(path).st_size > 0:
    print("Be careful")
else:
    print("OK!")

