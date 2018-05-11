import SenseFunction as ss

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

for i in range(len(measurements)):
    p = ss.sense(p, measurements[i])

print(p)


