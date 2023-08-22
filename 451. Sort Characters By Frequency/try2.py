'''
bucket sort
'''


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
                ct = ct+1
                dict.update({s[i]: ct})
            else:
                dict.update({s[i]: 1})

        print(dict)

        bucket = []

        for i in range(size+1):
            bucket.append([])

        for key, value in dict.items():
            bucket[value].append(key)

        print(bucket)

        for freq in range(size, 0, -1):
            num = len(bucket[freq])

            if num != 0:
                for j in range(num):
                    for k in range(freq):
                        output = output + bucket[freq][j]

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "tree"

    str2 = "eeeee"

    yeha = haha.frequencySort(str2)

    print("answer : \n\n")
    print(yeha)
