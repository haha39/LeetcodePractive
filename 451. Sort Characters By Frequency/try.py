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

        # print(dict)

        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        # print(sorted_dict)

        for key, value in sorted_dict:
            for i in range(value):
                output = output + key

        return output


if __name__ == '__main__':
    haha = Solution()
    str1 = "tree"

    str2 = "cccaaa"

    yeha = haha.frequencySort(str2)

    print("answer : \n\n")
    print(yeha)
