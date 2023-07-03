import numpy as np


class DP(object):
    def Fibonacci(self, n):

        np1 = np.ones(n)

        for i in range(2, n, 1):
            np1[i] = np1[i-1] + np1[i-2]

        print(np1)


if __name__ == '__main__':
    haha = DP()
    haha.Fibonacci(10)
