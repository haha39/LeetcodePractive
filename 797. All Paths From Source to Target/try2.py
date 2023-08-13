import copy


class Solution(object):
    def allPathsSourceTarget(self, graph):

        def bfs(rev_dir_graph, start, end, path):

            print("in bfs(), start is %d" % start)

            tmp = []
            for i in range(len(rev_dir_graph[start])):
                tmp.append([start]+path)

            i = 0
            for neighbor in rev_dir_graph[start]:
                # print(i)

                # print("in bfs(), neighbor is : %d" % neighbor)
                # print("tmp : ")
                # print(tmp)

                if neighbor != 0:

                    a = copy.deepcopy(path)
                    output = bfs(rev_dir_graph, neighbor, end, tmp[i])
                    print(output)
                    path = copy.deepcopy(a)
                    # print(a)
                    len0 = len(output)
                    tmp[i] = output[0]

                    for i in range(len0-1):
                        tmp.append(output[i+1])

                    # for i in range(len(output)):
                    # tmp[i] = output[0]
                    # print("????????")
                    # print(tmp)
                else:
                    # path.insert(0, 0)
                    tmp[i] = [0] + tmp[i]

                i = i + 1

                # print("hahahahaha : %d" % neighbor)
                # print(tmp)

            # print("tmp")
            # print(tmp)

            return tmp

        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # reverse direct graph in list rev_dir_graph

        rev_dir_graph = []
        size = len(graph)
        start = 0
        end = size - 1

        for i in range(size):
            rev_dir_graph.append([])

        for i in range(size):
            for j in graph[i]:
                rev_dir_graph[j].append(i)

        print("rev_dir_graph :")
        print(rev_dir_graph)

        # 0000
        all_path = []

        for neighbor in rev_dir_graph[end]:
            path1 = [end]

            print("neighbor0 : %d" % neighbor)

            if neighbor != 0:
                print("call bfs:")

                output = bfs(rev_dir_graph, neighbor, start, path1)
                all_path = all_path + output
            else:
                output = [[0, end]]
                all_path = all_path + output

            print("all_path:")
            print(all_path)
            print("\n")

        # print(output)

        return all_path


if __name__ == '__main__':

    haha = Solution()

    graph0 = [[1, 2], [3], [3], []]

    graph1 = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    graph2 = [[3, 1], [4, 6, 7, 2, 5], [4, 6, 3],
              [6, 4], [7, 6, 5], [6], [7], []]

    jojo = haha.allPathsSourceTarget(graph2)

    print("answer : \n\n")
    print(jojo)
