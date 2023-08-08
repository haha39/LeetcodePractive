class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.rooms = rooms

        output = Solution.dfs(self.rooms, 0)

        return output

    def dfs(graph, start):
        stack = []
        result = []

        stack.append(start)
        visited = set()
        visited.add(start)

        while (len(stack) > 0):
            currentVertex = stack.pop()
            result.append(currentVertex)

            for neighbor in graph[currentVertex]:
                if neighbor not in visited:

                    stack.append(neighbor)
                    visited.add(neighbor)

        return len(result) == len(graph)


if __name__ == '__main__':
    haha = Solution()
    rooms = [[1], [2], [3], []]

    nas = haha.canVisitAllRooms(rooms)

    print(nas)
