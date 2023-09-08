'''
1. put item with 0 indegree in queue
2. use bfs to check if we can solve the whole group altogather
3. 
'''


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        def topologicalSort():
            queue = []

            # indegree
            for g in range(-1, m, 1):
                for item in dict_group[g]:
                    if indegree[item] == 0:
                        queue.append(item)

            print(queue)

            while len(queue) != 0:
                tmp_queue = []

                current = queue.pop(0)
                print(current)

                current_group = group[current]
                print(current_group)

                if current_group == -1:
                    output.append(current)

                    for after in range(len(afterItem[current])):
                        indegree[after] -= 1
                        print(after)

            #     else:
            #         members = dict_group[current_group]
            #         print(members)
            #         #
            #         for i in members:
            #             if beforeItems[i] == []:
            #                 tmp_queue.append(i)

        # initial
        indegree = []
        afterItem = []
        dict_group = {}
        output = []

        # indegree
        for i in range(n):
            indegree.append(len(beforeItems[i]))

        # afterItem
        for i in range(n):
            afterItem.append([])

        for i in range(n):
            if beforeItems[i] != []:
                for j in beforeItems[i]:
                    afterItem[j].append(i)

        # dict_group
        for i in range(-1, m, 1):
            dict_group.update({i: []})

        for i in range(n):
            tmp = dict_group.get(group[i])
            tmp.append(i)
            dict_group.update({group[i]: tmp})

        print(indegree)
        print(afterItem)
        print(dict_group)

        topologicalSort()

        print(output)

        if len(output) != n:
            return []
        else:
            return output


if __name__ == '__main__':
    haha = Solution()
    # input1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

    print(group1)
    print(beforeItems1)

    nas = haha.sortItems(n1, m1, group1, beforeItems1)

    print("output1 : \n")
    print(nas)

    # input2
    n2 = 8
    m2 = 2
    group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems2 = [[], [6], [5], [6], [3], [], [4], []]

    # godspeed = haha.sortItems(n2, m2, group2, beforeItems2)
    # print(godspeed)
