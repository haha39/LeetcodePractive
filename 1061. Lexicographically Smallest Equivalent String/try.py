import numpy as np


class Solution(object):
    list1 = np.arange(26)

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        length = len(s1)
        str = ""

        # union
        for i in range(length):
            Solution.union(s1[i], s2[i])

    def find(num):
        x = 1

    def union(u, v):
        x = 1


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)

    x = np.arange(26)
    print(x)

    a = ord(s1[0]) - 97
    print(a)
