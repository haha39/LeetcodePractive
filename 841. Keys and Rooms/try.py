class Solution(object):
    def canVisitAllRooms(self, rooms):
        def dfs(graph, start):
            stack = []
            result = []
            visited = set()

            stack.append(start)
            visited.add(start)

            while (len(stack) > 0):
                currentVertex = stack.pop()
                result.append(currentVertex)

                for neighbor in graph[currentVertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)

            return len(result) == len(graph)

        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        #rooms

        output = dfs(rooms, 0)

        return output


if __name__ == '__main__':
    haha = Solution()
    rooms = [[1], [2], [3], []]

    nas = haha.canVisitAllRooms(rooms)

    print(nas)
