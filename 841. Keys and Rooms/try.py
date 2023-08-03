class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
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
        return result


if __name__ == '__main__':
    haha = Solution()
    haha.canVisitAllRooms(10)
