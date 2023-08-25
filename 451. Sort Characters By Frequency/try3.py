'''
heap / priority queue
'''


from heapq import heappush


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        size = len(s)
        output = ""

        for i in range(size):
            if s[i] in dict:
                ct = dict.get(s[i])
                ct = ct - 1
                dict.update({s[i]: ct})
            else:
                dict.update({s[i]: -1})

        print(dict)

        pq = []
        for key, value in dict.items():
            heappush(pq, (value, key))

        print(pq)

        len_pq = len(pq)

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "cbaa"

    str2 = "cccaaa"

    yeha = haha.frequencySort(str1)

    print("answer : \n\n")
    print(yeha)
