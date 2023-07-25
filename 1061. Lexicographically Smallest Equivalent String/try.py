import numpy as np

list1 = []
for i in range(26):
    list1.append(i)


class Solution(object):

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
            print(i)
            index1, index2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            Solution.union(index1, index2)

        # find

    def find(node):
        if node != list1[node]:
            list1[node] = Solution.find(list1[node])

        return list1[node]

    def union(u, v):
        root_u = Solution.find(u)
        root_v = Solution.find(v)

        print(root_u)
        print(root_v)

        if root_u < root_v:
            list1[v] = root_u
        elif root_u > root_v:
            list1[u] = root_v


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)

    x = np.arange(26)

    a = ord(s1[1]) - 97
    print(a)
