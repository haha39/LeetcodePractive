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

        def sortByGroup(id):
            '''
            Useing Topological Sort to order the members in the same group
            '''

            print("id = %d" % id)
            member = {}
            tmp = []
            sortedGroup = []
            size = 0

            # calucate size of group, indegree of members, and add 0-indegree-member to tmp
            for m in dict_group[id]:

                size += 1
                member[m] = indegree[m]

                if indegree[m] == 0:
                    tmp.append(m)

            print(member)
            print(tmp)
            print("size = %d" % size)

            # Topological Sort
            while len(tmp) != 0:
                x = tmp.pop()
                print(x)
                sortedGroup.append(x)
                for m in afterItem[x]:

                    in_degree = member.get(m, -100)

                    if in_degree == 1:  # this member can be sorted in the next round
                        tmp.append(m)
                    elif in_degree > 1:  # else, indegree--
                        in_degree -= 1
                        member[m] = in_degree

            print(sortedGroup)

            # return 1.the sorted group as list 2.size of this group
            return (sortedGroup, size)

        def enqueue(groupID):
            '''
            push id to queue if this id isn't in queue yet
            '''
            if groupID not in queue:
                queue.append(groupID)

        def enoutput(item):
            print("check it, item is %d" % item)
            if group[item] != -1:
                for after in afterItem[item]:
                    # print("yaya")
                    # 1. release afterItem
                    # 3. push in output
                    # need to fix this error : make a small loop/stack for group-1
                    indegree[after] -= 1
                output.append(item)
            else:
                stack = []
                stack.append(item)

                while (len(stack) != 0):

                    hito = stack.pop()
                    for after in afterItem[hito]:
                        if group[after] != -1:
                            indegree[after] -= 1
                        else:
                            stack.append(after)

                    output.append(hito)

        # initial
        afterItem = []
        dict_group = {}
        tmp_group = []
        indegree = []
        queue = []
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
        for i in range(m+1):
            tmp_group.append([])

        for i in range(n):
            tmp_group[group[i]+1].append(i)

        for i in range(m+1):
            dict_group[i] = tmp_group[i]

        print(indegree)
        print(afterItem)
        print(dict_group)

        # step1 : put group with 0 indegree into queue
        for groupID in range(m+1):

            getID = dict_group.get(groupID)

            if getID != None:
                for mem in getID:

                    if indegree[mem] == 0:
                        print("member %d's indegree is 0, in group %d" %
                              (mem, groupID))

                        if groupID == 0:
                            indegree[mem] = 0
                            enoutput(mem)

                            print(dict_group)
                            print(indegree)
                            print(output)
                        else:
                            enqueue(groupID)

        print(queue)
        print(output)

        # step2 : pop and try
        # while (len(queue) != 0):

        #     id = queue.pop(0)
        #     print("hey, this time id is %d\n" % id)
        #     res, size = sortByGroup(id)

        #     if len(res) == size:
        #         output = output + res
        #         print("jojo")
        #         for mem in res:
        #             # indegree = 0
        #             indegree[mem] = 0
        #             # enoutput
        #             # enoutput(mem)
        #             # check enqueue
        #             for after in afterItem[mem]:
        #                 if (group[after]+1) != id:
        #                     if group[after] != -1:
        #                         enqueue(after)
        #                     else:
        #                         enoutput(after)

        #     print("\nshow me the output")
        #     print(output)

        print("\ntemp output")
        print(output)

        return output if len(output) == n else []


if __name__ == '__main__':
    haha = Solution()
    # input1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

    # nas = haha.sortItems(n1, m1, group1, beforeItems1)

    # print("\nfinal output : \n")
    # print(nas)
    # print(group1)
    # print(beforeItems1)

    # input2
    n2 = 8
    m2 = 2
    group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems2 = [[], [6], [5], [6], [3], [], [4], []]

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
    group5 = [0, 1, 1, 2, 3, -1, 0, 0, 0, 1]
    beforeItems5 = [[2, 5], [3, 5, 4, 6, 8, 7, 2],
                    [7], [], [], [], [], [], [], []]

    # johnL = haha.sortItems(n5, m5, group5, beforeItems5)

    # print("\nfinal output : \n")
    # print(johnL)
    # print(grou5)
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
    # n7 = 5000
    # m7 = 152
    # group7 = []
    # beforeItems7 = []

    # flyingBanana = haha.sortItems(n7, m7, group7, beforeItems7)

    # print("\nfinal output : \n")
    # print(flyingBanana)

    # input8
    n8 = 5
    m8 = 5
    group8 = [2, 0, -1, 3, 0]
    beforeItems8 = [[2, 1, 3], [2, 4], [], [], []]

    gwen = haha.sortItems(n8, m8, group8, beforeItems8)

    print("\nfinal output : \n")
    print(gwen)
    print(group8)
    print(beforeItems8)
