import os
try:
    size = os.path.getsize('stream1.txt')
    print(f'The size = {size}')
except FileNotFoundError:
    print('File not exist.')
except OSError:
    print('OS error.')
# Lay du lieu tu file 1
ls1 = []
with open('stream1.txt', 'r') as f:
    while True:
        bit = f.read(1)
        if bit == '':
            break
        ls1.append(int(bit))
# Lay du lieu tu file 2
ls2 = []
with open('stream2.txt', 'r') as f:
    while True:
        bit = f.read(1)
        if bit == '':
            break
        ls2.append(int(bit))

# Tinh phan tram khac biet:
tong = 0
for i in range(len(ls1)):
    tong += abs(ls1[i] - ls2[i])
E = tong /len(ls1)* 100
print(f'Phan tram khac biet la: {E}%')