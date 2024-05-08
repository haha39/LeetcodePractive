'''
1. initial
2. Topological Sort to groups
3. Topological Sort to members in the sorted group order
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
            # make member without a group has a new group

            for i in range(n):
                if group[i] == -1:
                    group[i] = newSize
                    newSize += 1

            # return the number of how many groups there are now
            return newSize

        def sortByGroup(indegree, groupSize):
            # topological Sort to groups

            stack = []
            order = []

            for id in range(groupSize):
                if indegree[id] == 0:
                    stack.append(id)

            while len(stack) != 0:
                id = stack.pop()
                order.append(id)

                for after in afterGroup[id]:
                    indegree[after] -= 1

                    if indegree[after] == 0:
                        stack.append(after)

            # return the sorted group order
            return order

        def sortByItem(groupID):
            # topological Sort to members in this groupID

            stack = []
            tempOutput = []

            for member in groupMember[groupID]:  # initail
                if INmember[member] == 0:
                    stack.append(member)

            while len(stack) != 0:
                x = stack.pop()
                tempOutput.append(x)

                for mem in groupMember[groupID]:
                    if x in beforeItems[mem]:
                        INmember[mem] -= 1

                        if INmember[mem] == 0:
                            stack.append(mem)

            # return the sorted member order
            return tempOutput

        # step 1 : resign group id(mostly for member with -1 group)
        groupSize = reGroup(m)  # reGroup()

        # step 2 : topological Sort to groups
        INgroup = np.zeros(groupSize, dtype=int)
        afterGroup = []
        groupMember = []

        for i in range(groupSize):  # initail
            afterGroup.append([])
            groupMember.append([])

        for item in range(n):  # initail
            for before in beforeItems[item]:
                if group[before] != group[item]:
                    INgroup[group[item]] += 1
                    afterGroup[group[before]].append(group[item])

            groupMember[group[item]].append(item)

        groupOrder = sortByGroup(INgroup, groupSize)  # sortByGroup()

        # in case we can't sort all of the groups
        if len(groupOrder) != groupSize:
            return []

        # step3 : topological Sort to items in sorted groups
        INmember = []
        output = []

        for mem in range(n):  # initail
            indegree = 0

            for bef in beforeItems[mem]:
                if group[bef] == group[mem]:
                    indegree += 1

            INmember.append(indegree)

        for groupId in groupOrder:
            sortedMem = sortByItem(groupId)  # sortByItem()
            output += sortedMem

        # return output
        return output if len(output) == n else []


if __name__ == '__main__':

    haha = Solution()

    # input1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

    nas = haha.sortItems(n1, m1, group1, beforeItems1)

    print("\nfinal output :")
    print(nas)
    # print(group1)
    # print(beforeItems1)

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
