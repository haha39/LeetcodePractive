import numpy as np


class Solution(object):

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        list1 = np.arange(26)
        length = len(s1)
        str = ""

        # union
        for i in range(length):
            print(i)
            index1, index2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            print(index1)
            print(index2)
            Solution.union(list1, index1, index2)

        # find

    def find(list2, node):
        if node != list2[node]:
            list2[node] = Solution.find(list2[node])

        return list2[node]

    def union(list3, u, v):
        root_u = Solution.find(u)
        root_v = Solution.find(v)

        if root_u < root_v:
            list3[v] = root_u
        elif root_u > root_v:
            list3[u] = root_v


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)

    x = np.arange(26)

    a = ord(s1[1]) - 97
    print(a)
