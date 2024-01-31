import lightweight as lw
import time
ma = lw.light(0x1234567890abcdef)
s = time.time()
for _ in range(24576):
    ma.run()
e = time.time()
print(e - s)