import copy


class Solution(object):
    def allPathsSourceTarget(self, graph):
        def bfs(rverse_graph, start, end):

            size = start + 1
            queue = []
            result = []
            vertex = []

            for i in range(size):
                vertex.append([])
            vertex[-1].append(start)

            queue.append(start)

            while (len(queue) > 0):
                currentVertex = queue.pop(0)  # FIFS -> .pop(0)
                print("currentVertex : %d" % currentVertex)

                for neighbor in rverse_graph[currentVertex]:
                    print("neighbor : %d" % neighbor)

                    queue.append(neighbor)
                    tmp = copy.deepcopy(vertex[currentVertex])
                    tmp.insert(0, neighbor)

                    if neighbor == end:
                        result.append(tmp)

                    else:
                        vertex[neighbor] = copy.deepcopy(tmp)

                    vertex[currentVertex] = []  # clear
                    vertex[currentVertex].append(start)

            return result

        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # reverse direct graph in list rev_dir_graph
        rev_dir_graph = []
        size = len(graph)

        for i in range(size):
            rev_dir_graph.append([])

        for i in range(size):
            for j in graph[i]:
                rev_dir_graph[j].append(i)

        print(rev_dir_graph)

        # bfs(rev_dir_graph, (size-1), 0)

        return "hehe"


if __name__ == '__main__':
    haha = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    # a = []
    # a.append(1)
    # a.append(10)

    # a = copy.deepcopy(graph)
    # print(a)

    fish = haha.allPathsSourceTarget(graph)

    print(fish)
