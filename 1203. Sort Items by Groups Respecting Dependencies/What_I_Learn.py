'''
1. put item with 0 indegree in queue
2. use bfs to check if we can solve the whole group altogather
3. 
'''


import numpy as np


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        def reGroup(newSize):
            for i in range(n):
                if group[i] == -1:
                    group[i] = newSize
                    newSize += 1

            return newSize

        def sortByGroup(indegree, groupSize):
            a = 1
            stack = []
            order = []

            for id in range(groupSize):
                if indegree[id] == 0:
                    stack.append(id)

            print("\nsortByGroup, stack is : ")
            print(stack)

            while len(stack) != 0:

                id = stack.pop()
                order.append(id)

                for after in afterGroup[id]:

                    indegree[after] -= 1

                    if indegree[after] == 0:
                        stack.append(after)

            print("\nsortByGroup, group order:")
            print(order)

            return order

        def sortByItem(groupID):
            stack = []
            # for member in groupMember[groupID]:
            #     print(member)
            print(groupMember[groupID])

            return [5]

        # step 1 : resign group id(mostly for member with -1 group)
        groupSize = reGroup(m)
        print(group)
        print(groupSize)

        # step 2 : Topological Sort to groups
        INgroup = np.zeros(groupSize, dtype=int)
        afterGroup = []
        groupMember = []

        for i in range(groupSize):
            afterGroup.append([])
            groupMember.append([])

        for item in range(n):
            for before in beforeItems[item]:
                if group[before] != group[item]:
                    INgroup[group[item]] += 1
                    afterGroup[group[before]].append(group[item])

            groupMember[group[item]].append(item)

        print(INgroup)
        print(afterGroup)
        print(groupMember)

        groupOrder = sortByGroup(INgroup, groupSize)
        print(groupOrder)

        if len(groupOrder) != groupSize:  # in case
            return []

        # step3 : Topological Sort to items in sortes groups
        indegree = []
        output = []

        for i in range(n):
            indegree.append(len(beforeItems[i]))

        for groupId in groupOrder:

            sortedMem = sortByItem(groupId)
            output += sortedMem

        print(indegree)
        print(output)

        return output if len(output) == n else []


if __name__ == '__main__':

    haha = Solution()

    # input1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

    nas = haha.sortItems(n1, m1, group1, beforeItems1)

    print("\nfinal output : \n")
    print(nas)
    print(group1)
    print(beforeItems1)

    # input2
    n2 = 8
    m2 = 2
    # group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    # beforeItems2 = [[], [6], [5], [6], [3], [], [4], []]
    group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems2 = [[3], [6, 0], [5], [6], [3, 6, 7], [], [], []]

    # godspeed = haha.sortItems(n2, m2, group2, beforeItems2)
    # print("\nfinal output : \n")
    # print(godspeed)

    # input3
    n3 = 4
    m3 = 1
    group3 = [-1, 0, 0, -1]
    beforeItems3 = [[], [0], [1, 3], [2]]

    # RHCP = haha.sortItems(n3, m3, group3, beforeItems3)

    # print("\nfinal output : \n")
    # print(RHCP)
    # print(group3)
    # print(beforeItems3)

    # input4
    n4 = 5
    m4 = 3
    group4 = [0, 0, 2, 1, 0]
    beforeItems4 = [[3], [], [], [], [1, 3, 2]]

    # hangInTheAir = haha.sortItems(n4, m4, group4, beforeItems4)

    # print("\nfinal output : \n")
    # print(hangInTheAir)
    # print(group4)
    # print(beforeItems4)

    # input5
    n5 = 10
    m5 = 4
    # group5 = [0, 1, 1, 2, 3, -1, 0, 0, 0, 1]
    # beforeItems5 = [[2, 5], [3, 5, 4, 6, 8, 7, 2], [7], [], [], [], [], [], [], []]
    group5 = [2, 2, 2, 1, 0, 1, 3, 2, 0, 1]
    beforeItems5 = [[7, 6, 2, 5, 3], [], [], [], [7], [], [], [], [], []]

    # johnL = haha.sortItems(n5, m5, group5, beforeItems5)

    # print("\nfinal output : \n")
    # print(johnL)
    # print(group5)
    # print(beforeItems5)

    # input6
    n6 = 10
    m6 = 4
    group6 = [2, 2, 2, 1, 0, 1, 3, 2, 0, 1]
    beforeItems6 = [[7, 6, 2, 5, 3], [], [], [], [7], [], [], [], [], []]

    # gila = haha.sortItems(n6, m6, group6, beforeItems6)

    # print("\nfinal output : \n")
    # print(gila)

    # input7
    n7 = 5000
    m7 = 152
    group7 = []
    beforeItems7 = []

    # flyingBanana = haha.sortItems(n7, m7, group7, beforeItems7)

    # print("\nfinal output : \n")
    # print(flyingBanana)

    # input8
    n8 = 5
    m8 = 5
    group8 = [2, 0, -1, 3, 0]
    beforeItems8 = [[2, 1, 3], [2, 4], [], [], []]

    # gwen = haha.sortItems(n8, m8, group8, beforeItems8)

    # print("\nfinal output : \n")
    # print(gwen)
    # print(group8)
    # print(beforeItems8)
