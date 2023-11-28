from math import sqrt
from random import random
def approximate_pi(sample_size):
    hits = 0
    center = [0.5, 0.5]
    for _ in range(sample_size):
        sample = [random(), random()]
        dist = distance(sample, center)
        if dist < 0.5:
            hits += 1
    # area = pi * r^2
    # r = 0.5
    # r ^ 2 = 0.25
    # area = 0.25 pi
    # 4 area = pi
    area = hits / sample_size
    return 4 * area


def distance(x, y):
    return sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)


def main():
    print(approximate_pi(1000000))

main()