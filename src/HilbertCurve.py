import numpy as np
import array


class HilbertCurve:
    def __init__(self):
        self.generated = []
        self.generated.append(self.order1())

    def order1(self):
        output = []
        output.append([1, 2])
        output.append([0, 3])
        return output

    def mirrorVertical(self, input):
        output = []
        for i in range(len(input)):
            temp = []
            for j in range(len(input[0])-1, -1, -1):
                temp.append(input[i][j])
            output.append(temp)
        return output

    def rotate(self, input: array, clockwise: bool):
        output = []
        if clockwise:
            temp = self.mirrorVertical(input)
            for j in range(len(temp[0])):
                newTemp = []
                for i in range(len(temp)-1, -1, -1):
                    newTemp.append(temp[i][j])
                output.append(newTemp)
        else:
            temp = []
            for j in range(len(input[0])):
                newTemp = []
                for i in range(len(input) - 1, -1, -1):
                    newTemp.append(input[i][j])
                temp.append(newTemp)
            output = self.mirrorVertical(temp)
        return output

    def generate(self, order: int):
        if len(self.generated) >= order:
            return self.generated[order-1]

        if order == 1:
            return self.order1()

        lowerOrder = self.generate(order-1)
        clockwiseRotationLowerOrder = self.rotate(lowerOrder, True)
        counterClockwiseRotationLowerOrder = self.rotate(lowerOrder, False)

        size = [len(lowerOrder), len(lowerOrder[0])]
        topLeft = size[0]*size[1]
        topRight = size[0]*size[1]*2
        bottomRight = size[0]*size[1]*3

        output = []
        for i in range(size[0]*2):
            temp = []
            for j in range(size[1]*2):
                if i >= size[0] and j < size[1]: # bottom left
                    temp.append(clockwiseRotationLowerOrder[i-size[0]][j])
                elif i < size[0] and j < size[1]: # top left
                    temp.append(lowerOrder[i][j] + topLeft)
                elif i < size[0] and j >= size[1]: # top right
                    temp.append(lowerOrder[i][j-size[1]] + topRight)
                elif i >= size[0] and j >= size[1]: # bottom right
                    temp.append(counterClockwiseRotationLowerOrder[i-size[0]][j-size[1]] + bottomRight)
            output.append(temp)

        self.generated.append(output)
        print("new generated: " + str(order))
        return output
