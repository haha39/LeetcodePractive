class BS(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        left, right = price[0], price[-1]
        mid = (left + right) // 2

        if left == k:
            print("wryyyy")
        elif right == k:
            print("jojoooo")

        while (True):
            print(left, right, mid)

            if mid == k:
                print("yaaaa")
                break
            elif k > mid:
                left = mid+1
                mid = (mid + right) // 2
            elif k < mid:
                right = mid-1
                mid = (mid + left) // 2


if __name__ == '__main__':

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    haha = BS()
    haha.maximumTastiness(x, 2)
