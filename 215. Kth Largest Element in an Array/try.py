from heapq import heappop, heappush


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []

        for value in nums:
            heappush(pq, (-value))

        print(pq)

        for i in range(k):
            output = 0 - heappop(pq)

        return output


if __name__ == '__main__':
    haha = Solution()

    num1 = [3, 2, 1, 5, 6, 4]
    k1 = 2

    num2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4

    yeha = haha.findKthLargest(num1, k1)

    print("answer : \n")
    print(yeha)
