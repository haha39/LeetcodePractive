class Solution(object):

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        # initial value
        list1 = []
        for i in range(26):
            list1.append(i)

        len1 = len(s1)
        len2 = len(baseStr)
        str = ""

        # find with compression
        def find(node):
            if node != list1[node]:
                list1[node] = find(list1[node])

            return list1[node]

        # union by ascii
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u < root_v:
                list1[root_v] = root_u
            elif root_u > root_v:
                list1[root_u] = root_v

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
