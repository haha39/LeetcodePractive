import copy


class Solution(object):
    def allPathsSourceTarget(self, graph):
        def dfs(current, path):
            print(current)
            print(path)

            if current == end:  # end dfs()
                result.append(path)
                print("ya")
            else:
                size = len(graph[current])
                tmp = graph[current]

                for i in range(size):
                    neighbor = tmp[i]
                    dfs(neighbor, path + [neighbor])

        result = []
        end = len(graph) - 1

        dfs(0, [0])

        print(result)

        return result


if __name__ == '__main__':

    haha = Solution()

    graph0 = [[1, 2], [3], [3], []]

    graph1 = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    graph2 = [[3, 1], [4, 6, 7, 2, 5], [4, 6, 3],
              [6, 4], [7, 6, 5], [6], [7], []]

    jojo = haha.allPathsSourceTarget(graph1)

    print("answer : \n\n")
    print(jojo)
