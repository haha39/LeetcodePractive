import numpy as np


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # words = ["()()", "(())", "()()"]

        # a = list(set(words))
        # b = np.unique(words)
        # c = list(dict.fromkeys(words))
        # d = []
        # [d.append(x) for x in words if x not in d]

        # # print(a)
        # # print(b)
        # # print(c)
        # # print(d)

        # # len1 = len(words)
        # # print(len1)

        result = []

        result.append(["()"])
        # # print(result)

        for i in range(1, n, 1):
            # print(i)
            tmp = []
            length = len(result[i-1])
            # print(length)

            for j in range(length):
                str1 = "()" + result[i-1][j]
                str2 = "(" + result[i-1][j] + ")"
                str3 = result[i-1][j] + "()"
                tmp.append(str1)
                tmp.append(str2)
                tmp.append(str3)

            # print(tmp)
            result.append(list(set(tmp)))
            # print(result)

        return result[n-1]


if __name__ == '__main__':
    haha = Solution()
    ya = haha.generateParenthesis(4)

    print(ya)


'''
1
2
3 : (2), 1 X 2
4 : (3), 1 X 3, 2 X 2
'''
