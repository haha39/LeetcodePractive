class Solution(object):
    def allPathsSourceTarget(self, graph):
        def bfs(rverse_graph, start, end):

            size = start + 1
            queue = []
            result = []
            node = []

            for i in range(size):
                node.append([start])

            queue.append(start)

            while (len(queue) > 0):
                currentVertex = queue.pop(0)  # FIFS -> .pop(0)
                tmp = []
                tmp.append(currentVertex)

                for neighbor in rverse_graph[currentVertex]:
                    queue.append(neighbor)

                    if neighbor == end:
                        node[currentVertex].insert(0, end)
                        result.append(tmp)
                    else:
                        node[currentVertex].insert(0, neighbor)

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

        bfs(rev_dir_graph, (size-1), 0)

        return "hehe"


if __name__ == '__main__':
    haha = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    fish = haha.allPathsSourceTarget(graph)

    print(fish)
