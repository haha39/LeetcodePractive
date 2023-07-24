import numpy as np

list1 = np.arange(26)


class Solution(object):

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        print(list1)
        length = len(s1)
        str = ""
        Solution.happy()
        print(list1)

        # union
        for i in range(length):
            # print(i)
            index1, index2 = ord(s1[i]) - 97, ord(s2[i]) - 97

            # Solution.union(index1, index2)

        # find
    def happy():
        for i in range(26):
            list1[i] += 10

    # def find(list2, node):
    #     if node != list2[node]:
    #         list2[node] = Solution.find(list2[node])

    #     return list2[node]

    # def union(list3, u, v):
    #     root_u = Solution.find(u)
    #     root_v = Solution.find(v)

    #     if root_u < root_v:
    #         list3[v] = root_u
    #     elif root_u > root_v:
    #         list3[u] = root_v


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)

    x = np.arange(26)

    a = ord(s1[1]) - 97
    print(a)
