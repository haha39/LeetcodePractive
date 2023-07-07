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
            print("round : %d" % i)
            # step1
            tmp = []
            last = i - 1
            len_last = len(result[last])

            for j in range(len_last):
                str1 = "(" + result[i-1][j] + ")"
                tmp.append(str1)

            # step2
            len_half = int(n/2)
            print("len_half : %d" % len_half)

            for j in range(len_half):
                x = j
                y = i - j - 1
                print("x : %d" % x)
                print("y : %d" % y)

                len_x = len(result[x])
                len_y = len(result[y])

                for a in range(len_x):
                    for b in range(len_y):
                        str2 = result[x][a] + result[y][b]
                        str3 = result[y][b] + result[x][a]
                        tmp.append(str2)
                        tmp.append(str3)

            # step3
            # print(tmp)
            result.append(list(set(tmp)))
            # print(result)

        return result[n-1]
        # return int(5/2)


if __name__ == '__main__':
    haha = Solution()
    ya = haha.generateParenthesis(3)

    print(ya)


'''
1
2
3 : (2), 1 X 2
4 : (3), 1 X 3, 2 X 2
5 : (4), 1 X 4, 2 X 3
6 : (5), 1 X 5, 2 X 4, 3 X 3
'''
