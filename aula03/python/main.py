#!/usr/bin/env python3
import matplotlib.pyplot as plt
import cv2
import numpy as np
FILE_PATH = "../resources/lenna.png"


class Histogram:
    def __init__(self, nChannel):
        self.nChannel = nChannel
        self.histChannel = None

    def __mask(self):
        """Método interno para inicializar a Lista de histograma com valor inicial 0
            Parameters
            ----------
            channel: int
        """
        hist = []

        for channel in range(self.nChannel):
            hist.append([])
            hist[channel] = [0] * 256

        return hist

    def getChannel(self, channel):
        """Método para retornar os valores de acordo com os canais(RGB) da imagem
            Parameters
            ----------
            channel: int
        """
        return self.histChannel[channel]

    def generateFrom(self, matrix):
        """Método para criar histograma a partir de uma matriz
            Parameters
            ----------
            matrix : list[list]
                Lista de lista de canais que contém a quantidade de cor [0-255].
                Exemplo: [[0,0,255],[1,24,45],...]
        """
        hist = self.__mask()
        for line in range(len(matrix)):
            for pixel in matrix[line]:
                for channel in range(self.nChannel):
                    hist[channel][pixel[channel]] += 1
        self.histChannel = hist

    def __str__(self):
        if(self.histChannel is None):
            return "histograma não disponível"
        else:
            return "Red: %s \n Green: %s \nBlue: %s\n" % (self.histChannel[0], self.histChannel[1], self.histChannel[2])


class ImageTool:
    def changeExposure(self, matrix, nChannel):
        copymatrix = matrix
        for line in range(len(matrix)):
            for pixel in matrix[line]:
                for channel in range(nChannel):
                    copymatrix[channel][pixel[channel]] -= 255
        return copymatrix


class Question:
    def solve_1(self, img):
        hist = Histogram(3)
        hist.generateFrom(img)
        plt.figure()
        plt.subplot(511)
        plt.bar(range(256), hist.getChannel(2), width=1.0,
                facecolor='red', edgecolor='red')
        plt.ylabel('Frequência')
        plt.xlabel('Red')
        plt.subplot(513)
        plt.bar(range(256), hist.getChannel(1), width=1.0,
                facecolor='green', edgecolor='green')
        plt.ylabel('Frequência')
        plt.xlabel('Green')
        plt.subplot(515)
        plt.bar(range(256), hist.getChannel(0), width=1.0,
                facecolor='blue', edgecolor='blue')
        plt.ylabel('Frequência')
        plt.xlabel('Blue')
        plt.show()

    def solve_2(self, img, num):
        cv2.imshow('image', ImageTool().changeExposure(img, 3))
        cv2.waitKey(0)


def main():
    # OPENCV uses BGR not RGB
    img = cv2.imread(FILE_PATH)

    questions = Question()
    questions.solve_2(img, 20)


if __name__ == "__main__":
    main()
