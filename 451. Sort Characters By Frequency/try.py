class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map1 = {}
        size = len(s)
        output = []

        for i in range(size):
            if s[i] in map1:
                ct = map1.get(s[i])
                ct = ct+1
                map1.update({s[i]: ct})
            else:
                map1.update({s[i]: 1})

        print(map1)

        tt = sorted(map1.items(), key=lambda x: x[1], reverse=True)

        print(tt)

        for key, value in tt:
            for i in range(value):
                output.append(key)

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "tree"

    str2 = "cccaaa"

    yeha = haha.frequencySort(str1)

    print("answer : \n\n")
    print(yeha)
