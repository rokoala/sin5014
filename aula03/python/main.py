#!/usr/bin/env python3

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

FILE_PATH = "../resources/lenna.png"


def histogram(matrix):
    hist = [[]]
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):

            hist[0][matrix[line][column][0]] += 1
           # hist[1][matrix[line][column][1]] += 1
           # hist[2][matrix[line][column][2]] += 1
    return hist


# aImg = mpimg.imread(FILE_PATH)
aImg = plt.imread(FILE_PATH)
plt.imshow(aImg)
plt.show()
# histogram(aImg)
