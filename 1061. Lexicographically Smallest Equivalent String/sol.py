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
        len1 = len(s1)
        len2 = len(baseStr)
        str = ""

        # union
        for i in range(len1):
            print(i)
            index1, index2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            Solution.union(index1, index2)

            print(list1)

        # find
        for i in range(len2):
            num = ord(baseStr[i]) - 97
            num = Solution.find(num)
            num = num + 97
            str = str + chr(num)

        print(str)

    def find(node):
        if node != list1[node]:
            list1[node] = Solution.find(list1[node])

        return list1[node]

    def union(u, v):
        root_u = Solution.find(u)
        root_v = Solution.find(v)

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
