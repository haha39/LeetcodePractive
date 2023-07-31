class Disjoin:

    def __init__(self) -> None:
        self.parent = [i for i in range(26)]

    # find with compression
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    # union by ascii
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u < root_v:
            self.parent[root_v] = root_u
        elif root_u > root_v:
            self.parent[root_u] = root_v


class Solution(object):

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        ds = Disjoin()
        len1 = len(s1)
        len2 = len(baseStr)
        str = ""

        # union s1 and s2
        for i in range(len1):
            # print(i)
            index1, index2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            union(index1, index2)

        # find by baseStr
        for i in range(len2):
            num = ord(baseStr[i]) - 97
            num = find(num)
            num = num + 97
            str = str + chr(num)

        # print(str)
        return str


if __name__ == '__main__':

    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"

    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)
