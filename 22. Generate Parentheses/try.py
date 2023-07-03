import numpy as np


class DP(object):
    def Fibonacci(self, n):

        # np
        np1 = np.zeros(n)

        print(np1)
        np1[0] = 1
        np1[1] = 1

        for i in range(2, n, 1):
            np1[i] = np1[i-1] + np1[i-2]

        print(np1)


if __name__ == '__main__':
    haha = DP()
    haha.Fibonacci(10)
