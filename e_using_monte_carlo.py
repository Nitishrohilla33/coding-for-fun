# approximate value of e using monte carlo method
import numpy as np
experiments,batch_size,counts = 10000000, 1000000, []
remaining = experiments
while remaining > 0:
    size = min(batch_size, remaining)   
    s,c = np.zeros(size), np.zeros(size, dtype=int) 
    active = np.ones(size, dtype=bool)  
    while np.any(active):
        r = np.random.uniform(0, 1, size)
        s[active] += r[active]
        c[active] += 1
        active = s < 1
    counts.append(c)
    remaining -= size
counts = np.concatenate(counts)
print(np.mean(counts))
print(np.e)