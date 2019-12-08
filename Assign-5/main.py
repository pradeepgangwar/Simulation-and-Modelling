## Submitted by IHM2016501 | Pradeep Gangwar

import os
import random

# Function implementing the mixed LCG algorithm
def mixed_lcg(a, m, c, seed):
    f = open('mixed_lcg.txt', 'w')
    
    for i in range (1000):
        seed = (a * seed + c) % m
        f.write(str(seed) + '\n')
    f.close()

# Function implementing the additive LCG algorithm
def additive_lcg(a, m, seed):
    f = open('additive_lcg.txt', 'w')

    numbers = []
    numbers.append(seed)
    numbers.append(0.756)
    f.write(str(numbers[0]) + '\n')
    f.write(str(numbers[1]) + '\n')
    
    for i in range (2, 1001):
        seed = (numbers[i-1] + numbers[i-2]) % m
        numbers.append(seed)
        f.write(str(numbers[i]) + '\n')
    f.close()

# Function implementing the multiplicative LCG algorithm
def multiplicative_lcg(a, m, c, seed):
    f = open('multiplicative_lcg.txt', 'w')

    for i in range (1000):
        seed = (a * seed + c) % m
        f.write(str(seed) + '\n')
    f.close()

# Function implementing the default random number generator of python
def default_generator(seed):
    f = open('default_generator.txt', 'w')

    random.seed(seed)
    for i in range(1000):
        number = random.uniform(0,1)
        f.write(str(number) + '\n')
    f.close()

###################
## Main Function ##
###################
if __name__=='__main__':
    a = 2.96
    m = 1.0
    c = 0.25
    seed = 0.342

    mixed_lcg(a, m, c, seed)

    additive_lcg(a, m, seed)

    multiplicative_lcg(a, m, 0, seed)

    default_generator(seed)

