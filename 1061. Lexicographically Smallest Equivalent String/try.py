class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


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

        for i in range(length):
            Solution.union(s1[i], s2[i])

    def find(self, element):
        return self._find(self.sets[element])

    def _find(self, n):
        if n.parent != n:
            # path compression
            n.parent = self._find(n.parent)
        return n.parent

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.parents[u] = v
            self.count -= 1


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)
