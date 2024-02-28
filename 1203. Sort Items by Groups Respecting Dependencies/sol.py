import copy

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

        def topologicalSort(indegree):
            queue = []
            output = []

        def sortByGroup():
            x = 5

        def enoutput(output, item, groupID):
            if groupID == 0:
                for i in afterItem[item]:
                    print("yaya")
                    # 1. release afterItem
                    # 2. delete in dict_group
                    # 3. push in output

        def enqueue(queue, groupID):
            if groupID not in queue:
                queue.append(groupID)
            return queue

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
            dict_group[i-1] = tmp_group[i]

        print(indegree)
        print(afterItem)
        print(dict_group)

        # step1 : put group with 0 indegree into queue
        for i in range(m+1):
            for j in dict_group.get(i-1):
                if j != None:
                    if indegree[j] == 0:
                        print(j)

                        if i == 0:
                            enoutput(output, j, i)
                            print(dict_group)
                            print(indegree)
                            print(output)
                        else:
                            enqueue(queue, i)

        print(queue)

        # print("\ntemp output")
        # print(ans)

        # if len(ans) != n:
        #     return []
        # else:
        #     return ans


if __name__ == '__main__':
    haha = Solution()
    # input1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]

    print(group1)
    print(beforeItems1)

    # aa = {}
    # h = ['haha', 'hehe', 'jojo']

    # aa['haha'] = 1
    # aa['hehe'] = 1

    # for i in h:
    #     x = aa.get(i)
    #     print(h[x])
    #     print(type(x))

    nas = haha.sortItems(n1, m1, group1, beforeItems1)

    print("\nfinal output : \n")
    print(nas)
    print(group1)
    print(beforeItems1)

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
