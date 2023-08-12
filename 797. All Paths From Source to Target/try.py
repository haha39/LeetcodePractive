class Solution(object):
    def allPathsSourceTarget(self, graph):
        def bfs(graph, start):

            queue = []
            result = []
            visited = set()

            queue.append(start)
            visited.add(start)

            while (len(queue) > 0):
                currentVertex = queue.pop(0)
                result.append(currentVertex)

                for neighbor in graph[currentVertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

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
