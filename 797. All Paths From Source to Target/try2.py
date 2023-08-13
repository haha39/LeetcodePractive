import copy


class Solution(object):
    def allPathsSourceTarget(self, graph):

        def bfs(rev_dir_graph, start, end, path):
            print("in bfs(), start is %d" % start)
            print("path : ")
            print(path)

            for neighbor in rev_dir_graph[start]:
                print("in bfs(), neighbor is : %d" % neighbor)
                path.insert(0, start)

                if neighbor != 0:
                    output = bfs(rev_dir_graph, neighbor, end, path)
                    path = output + path
                else:
                    path.insert(0, 0)

                print("path : ")
                print(path)

            return path

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
        path = [end]

        for neighbor in rev_dir_graph[end]:
            print("neighbor0 : %d" % neighbor)

            if neighbor != 0:
                print("call bfs:")
                output = bfs(rev_dir_graph, neighbor, start, path)
                all_path.append(output)
            else:
                output = [0, end]
                all_path.append(output)

            print("all_path:")
            print(all_path)

        # print(output)

        return output


if __name__ == '__main__':
    haha = Solution()
    graph1 = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    graph2 = [[3, 1], [4, 6, 7, 2, 5], [4, 6, 3],
              [6, 4], [7, 6, 5], [6], [7], []]

    a = []
    a.append(1)

    b = [2, 3]

    c = a + b

    print(c)

    fish = haha.allPathsSourceTarget(graph1)

    print("answer : \n\n")
    print(fish)
