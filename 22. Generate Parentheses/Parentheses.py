import numpy as np


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        words = ["()()", "(())", "()()"]
        a = set(words)
        b = np.unique(words)

        print(a)
        print(b)


if __name__ == '__main__':
    haha = Solution()
    haha.generateParenthesis(1)
