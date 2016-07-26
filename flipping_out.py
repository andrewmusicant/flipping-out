import math
import random
import statistics as st
import numpy as np
# import matplotlib.pyplot as plt

record = []
count = 0
heads_record = []
tails_record = []


def flip_coin():
    x = random.randint(1, 2)
    return x


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


def simulation(count):
    heads = 0
    tails = 0
    n = 2**16
    while count < n:
        x = flip_coin()
        if is_power2(count):
            print(heads, tails)
            heads_record.append(heads)
            tails_record.append(tails)
        if x == 1:
            heads += 1
        else:
            tails += 1
        count += 1

    return heads, tails

x, y = simulation(count)
points = list(zip(heads_record, tails_record))
single_points = [x1 - x2 for (x1, x2) in zip(heads_record, tails_record)]
ratio_points = [x1 / x2 for (x1, x2) in zip(heads_record, tails_record) if x2 != 0]
print(points)
print("heads", x, "tails", y)
# print(record)
