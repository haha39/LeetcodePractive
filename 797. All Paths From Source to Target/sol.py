import copy


class Solution(object):
    def allPathsSourceTarget(self, graph):

        def dfs(start, path):

            if graph[start] == size-1:  # end node
                result.append(path+start)
            else:
                for i in range(len(graph[start])):
                    path = path + start

        result = []
        size = len(graph)

        dfs(0, [0])

        return result


if __name__ == '__main__':

    haha = Solution()

    graph0 = [[1, 2], [3], [3], []]

    graph1 = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    graph2 = [[3, 1], [4, 6, 7, 2, 5], [4, 6, 3],
              [6, 4], [7, 6, 5], [6], [7], []]

    jojo = haha.allPathsSourceTarget(graph2)

    print("answer : \n\n")
    print(jojo)
