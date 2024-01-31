import os
import math
try:
    size = os.path.getsize('stream1.txt')
    print(f'The size: {size}')
except FileNotFoundError:
    print("File not found.")
except OSError:
    print("OS error occured.")

def Average(lis):
    return sum(lis) /len(lis)

ls1 = []
with open('stream1.txt', 'r') as f:
    while True:
        read = f.read(1)
        if (read == ''):
            break
        ls1.append(int(read))
av1 = Average(ls1)
ls2 = []
with open('stream2.txt', 'r') as f:
    while True:
        read = f.read(1)
        if (read == ''):
            break
        ls2.append(int(read))
av2 = Average(ls2)
cov = 0
da = 0
db = 0
for i in range(len(ls1)):
    tu1 = (ls1[i] - av1)
    tu2 = ls2[i] - av2
    cov = cov + tu1 *tu2
    da = da + tu1**2
    db = db + tu2**2

corr = cov/(math.sqrt(da)*math.sqrt(db))
print(corr)
