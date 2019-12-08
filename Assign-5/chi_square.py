## Submitted by IHM2016501 | Pradeep Gangwar

import os
import sys

expected = 100

## Chi square base function
def calculate(observed, expected):
    return (observed - expected)**2 / expected

## COunting the numbers in each class
def count_observed(numbers):
    count = []
    for i in range(10):
        l = len(list(x for x in numbers if 0.1*i <= x < 0.1*(i+1))) 
        count.append(l)
    return count

## Sigma function of chi square
def calc_chi_square(count):
    s = 0
    for val in count:
        s += calculate(val, expected)
    print(s)


###################
## Main Function ##
###################
if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename, 'r')

    numbers = []
    line = f.readline()
    while(line != ""):
        numbers.append(float(line[:-1]))
        line = f.readline()
    f.close()

    count_list = count_observed(numbers)
    calc_chi_square(count_list)
