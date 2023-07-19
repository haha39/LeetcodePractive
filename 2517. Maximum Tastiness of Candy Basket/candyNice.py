'''
in my mind : 
we need two part
partA is BS, the goal is to find the needed number
partB is to check whether the number can fit the tasteness of k candies or not
'''


class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """

        def BS_check(temp_min):
            last, ct, i = price[0], 1, 1

            while ct < k and i < len(price):
                if price[i] - last >= temp_min:
                    last = price[i]
                    ct += 1

            return (ct == k)

        lo, hi = 0, 10 ** 9
        price.sort()

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if BS_check(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1


if __name__ == '__main__':

    x = [13, 5, 1, 8, 21, 2]
    haha = Solution()
    output = haha.maximumTastiness(x, 3)

    print(output)
