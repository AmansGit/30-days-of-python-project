from math import exp, sin
import time
def calculate_time(a):
    res = 0
    for val in a:
        res += exp(val) * sin(val)
    yield res


x = [0.1 * i for i in range(1000)]
t0 = time.process_time()
for r in range(1000):
    calculate_time(x)
t1 = time.process_time()
print("Time spent", t1-t0)

