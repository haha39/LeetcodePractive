'''
heap / priority queue
'''


from heapq import heappop, heappush


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

        # print(dict)

        pq = []
        for key, value in dict.items():
            heappush(pq, (value, key))

        # print(heappop(pq))

        len_pq = len(pq)

        for i in range(len_pq):
            # it's a heap!!!!! you have to use 'pop' instead of [0],[1],[2]
            freq, char = heappop(pq)

            for j in range(freq, 0, 1):
                output = output + char

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "cbaa"

    str2 = "cccaaa"

    str3 = "raaeaedere"

    yeha = haha.frequencySort(str3)

    print("answer : \n")
    print(yeha)
