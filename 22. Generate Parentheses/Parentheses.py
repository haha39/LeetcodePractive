import numpy as np


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        words = ["()()", "(())", "()()"]

        a = list(set(words))
        b = np.unique(words)
        c = list(dict.fromkeys(words))
        d = []
        [d.append(x) for x in words if x not in d]

        print(a)
        print(b)
        print(c)
        print(d)


if __name__ == '__main__':
    haha = Solution()
    haha.generateParenthesis(1)
