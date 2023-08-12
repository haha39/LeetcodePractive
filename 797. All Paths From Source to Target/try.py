class Solution(object):
    def allPathsSourceTarget(self, graph):
        def bfs(graph, start, end):
            queue = []
            result = []

            queue.append(start)

            while (len(queue) > 0):
                currentVertex = queue.pop(0)  # FIFS -> .pop(0)
                result.append(currentVertex)

                for neighbor in graph[currentVertex]:
                    if neighbor == start:
                        # queue.append(neighbor)
                        x = 0

            return result

        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """


if __name__ == '__main__':
    haha = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    fish = haha.allPathsSourceTarget(graph)

    print(fish)
