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
                    print("%d\t%d" % (item, indegree[item]))
                    if indegree[item] == 0:
                        queue.append(item)

            # print(queue)

            while len(queue) != 0:
                print("\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiin queue :")
                print(queue)

                current = queue.pop(0)
                print("current : %d" % current)

                current_group = group[current]
                print("current_group : %d" % current_group)

                if current_group == -1:
                    output.append(current)

                    for after in afterItem[current]:
                        print(after)
                        indegree[after] -= 1
                        if indegree[after] == 0:
                            queue.append(after)

                    print(output)
                    print(indegree)
                    print(queue)
                    print("if enddddddddddddddddddddddddddddddddddd")
                else:  # check()
                    tmp_queue = []
                    tmp_output = []
                    tmp_indegree = copy.deepcopy(indegree)
                    members = copy.deepcopy(dict_group[current_group])
                    members.remove(current)

                    print("same members :")
                    print(members)

                    for mem in afterItem[current]:
                        tmp_indegree[mem] -= 1
                        if tmp_indegree[mem] == 0 and mem in members:
                            tmp_queue.append(mem)

                        print("member : %d" % mem)
                        print("tmp_indegree[%d] : %d" %
                              (mem, tmp_indegree[mem]))
                    print(tmp_queue)

                    tmp_output.append(current)

                    print("now members :")
                    print(members)
                    print("now tmp_queue :")
                    print(tmp_queue)

                    while len(tmp_queue) != 0:
                        tmp_current = tmp_queue.pop()
                        tmp_output.append(tmp_current)
                        members.remove(tmp_current)

                        for after in afterItem[tmp_current]:
                            tmp_indegree[after] -= 1

                            if tmp_indegree[after] == 0:
                                tmp_queue.append(after)

                        print("tmp_queue")
                        print(tmp_queue)
                        print("tmp_output")
                        print(tmp_output)
                        print("members")
                        print(members)

                    # check if group in current be all add in tmp_output
                    if len(members) != 0:
                        queue.append(current)
                    else:
                        output = output + tmp_output

                        # tmp_indegree
                        indegree = copy.deepcopy(tmp_indegree)

                        # big remove from queue
                        for ok in tmp_output:
                            if ok in queue:
                                queue.remove(ok)
                        # help afterItem of member in the group
                        for mem in tmp_output:
                            for after in afterItem[mem]:
                                if indegree[after] == 0 and after not in output:
                                    queue.append(after)

                        print(indegree)
                        print(queue)
                        print(output)

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
    # print(godspeed)
