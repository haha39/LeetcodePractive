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
            Solution.union(s1[i], s2[i])

    def find(self, element):
        x = 1

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if u < v:
                self.parents[v] = u
            else:
                self.parents[u] = v

            self.count -= 1


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    haha = Solution()
    haha.smallestEquivalentString(s1, s2, baseStr)
