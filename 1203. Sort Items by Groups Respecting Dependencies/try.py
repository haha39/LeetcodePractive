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

            for g in range(-1, m, 1):
                for item in dict_group[g]:
                    # print("%d\t%d" % (item, indegree[item]))
                    if indegree[item] == 0:
                        queue.append(item)

            # print(queue)

            while len(queue) != 0:
                # print("\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiin queue :")
                # print(queue)

                current = queue.pop(0)
                # print("current : %d" % current)

                current_group = group[current]
                # print("current_group : %d" % current_group)

                if current_group == -1:
                    output.append(current)

                    for after in afterItem[current]:
                        # print(after)
                        indegree[after] -= 1
                        if indegree[after] == 0:
                            queue.append(after)

                    # print(output)
                    # print(indegree)
                    # print(queue)
                    # print("if enddddddddddddddddddddddddddddddddddd")
                else:  # check()
                    tmp_queue = []
                    tmp_output = []
                    tmp_indegree = copy.deepcopy(indegree)
                    members = copy.deepcopy(dict_group[current_group])
                    members.remove(current)

                    # print("same members :")
                    # print(members)

                    for after in afterItem[current]:
                        tmp_indegree[after] -= 1

                    for mem in members:
                        if tmp_indegree[mem] == 0:
                            tmp_queue.append(mem)

                        # print("member : %d" % mem)
                        # print("tmp_indegree[%d] : %d" %
                        #       (mem, tmp_indegree[mem]))

                    tmp_output.append(current)

                    # print("now members :")
                    # print(members)
                    # print("now tmp_queue :")
                    # print(tmp_queue)

                    while len(tmp_queue) != 0:
                        tmp_current = tmp_queue.pop()
                        tmp_output.append(tmp_current)
                        members.remove(tmp_current)

                        for after in afterItem[tmp_current]:
                            tmp_indegree[after] -= 1
                        for mem in members:
                            if tmp_indegree[mem] == 0 and mem not in tmp_queue:
                                tmp_queue.append(mem)

                        # print("tmp_queue")
                        # print(tmp_queue)
                        # print("tmp_output")
                        # print(tmp_output)
                        # print("members")
                        # print(members)

                    # check if group in current be all add in tmp_output
                    if len(members) == 0:
                        # print("else almost end")
                        # print(tmp_output)

                        output = output + tmp_output

                        # tmp_indegree
                        indegree = copy.deepcopy(tmp_indegree)

                        # help all member with indegree = 0 and not yet in output
                        for mem in range(n):
                            if (mem not in output) and (mem not in queue) and (indegree[mem] == 0):
                                queue.append(mem)

                        # big remove from queue
                        for ok in tmp_output:
                            if ok in queue:
                                queue.remove(ok)

                        # print(indegree)
                        # print(queue)
                        # print(output)

            return output

        # initial
        afterItem = []
        dict_group = {}

        indegree = []

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

        ans = topologicalSort(indegree)

        print("\ntemp output")
        print(ans)

        if len(ans) != n:
            return []
        else:
            return ans


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
