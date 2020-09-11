import math
import random
import numpy as numpy

u = int(input("Enter value for u:"))
k = int(input("Enter value for k:"))
c = int(input("Enter value for c:"))
interval_width = int(input("Enter the interval:"))
iterations = []
interval = interval_width + 1

def micro(u, k, c):
    nbrThrows = 0
    b = math.pow(2, u)
    micromints = {}
    for x in range(int(b)+1):
        micromints[x] = 0
    createdCoins = 0
    while createdCoins != c:
        randomBin = random.randint(0, b)
        nbrThrows += 1
        micromints[randomBin] += 1
        if(micromints[randomBin] == k):
            createdCoins += 1
            if createdCoins == c:
                iterations.append(nbrThrows)
                break


def get_confidence_interval():
    lambdaVar = 3.66
    var = lambdaVar * (numpy.std(iterations) / math.sqrt(len(iterations)))
    interval_var = (numpy.mean(iterations) + var) - \
            (numpy.mean(iterations) - var)
    if interval_var == 0:
        interval_var = interval

    return int(interval_var)


def main(interval):
    sum = 0
    while interval > interval_width:
        micro(u, k, c)
        interval = get_confidence_interval()

    print(numpy.mean(iterations))

main(interval)
