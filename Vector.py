import numpy as np


def valid(function):
    
    def check(self, other):
        if len(self.vector) == len(other.vector):
            return function(self, other)
        else:
            raise TypeError("Unsupported operands error - Vectors must be the same dimension")
    return check


class Vector:
    def __init__(self, *args):
        self.vector = list(*args)

    @valid
    def __add__(self, other):
        vector_sum = []
        for i in zip(self.vector, other.vector):
            vector_sum.append(sum(i))
        return vector_sum

    @valid
    def __sub__(self, other):
        vector_sub = []
        for i in zip(self.vector, other.vector):
            vector_sub.append(i[0] - i[1])
        return vector_sub

    @valid
    def __matmul__(self, other):
        vector_matmul = 0
        for i in zip(self.vector, other.vector):
            vector_matmul += i[0] * i[1]
        return vector_matmul

    @valid    
    def __mul__(self, other):
        vector_mul = np.cross(self.vector, other.vector)
        return vector_mul


v1 = Vector([2, 3, -1])
v2 = Vector([5, 1, 5])
v3 = v1 + v2
print(v3)
