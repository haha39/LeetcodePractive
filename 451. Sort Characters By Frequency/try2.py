'''
bucket sort
'''


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map1 = {}
        size = len(s)
        output = ""

        for i in range(size):
            if s[i] in map1:
                ct = map1.get(s[i])
                ct = ct+1
                map1.update({s[i]: ct})
            else:
                map1.update({s[i]: 1})

        print(map1)

        bucket = []

        for i in range(size):
            bucket.append([])

        for i in range(size):
            freq = map1[i]

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "tree"

    str2 = "cccaaa"

    yeha = haha.frequencySort(str1)

    print("answer : \n\n")
    print(yeha)
