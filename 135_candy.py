import unittest

class Solution:
    def candy(self, ratings) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
            
        return sum(candy)


class Solution2:
    def candy(self, ratings) -> int:
        graph = self.build_graph(ratings)
        return self.calc_sum(graph, ratings)
        
    def build_graph(self, ratings):
        graph = {
            'root': []
        }
        for i, r in enumerate(ratings):
            graph[i] = []
            r = ratings[i]
            if (i > 0) and (r > ratings[i-1]):
                graph[i-1].append(i)
            else:
                if (i > 0) and (r < ratings[i-1]):
                    graph['root'].append(i)
                    graph[i].append(i-1)
                    if (i-1) in graph['root']:
                        graph['root'].remove(i-1)
                else:
                    graph['root'].append(i)
        return graph
    
    def calc_sum(self, graph, ratings):
        sum = 0
        sums = {}
        queue = [('root', 0)]
        depth = 0
        while queue:
            node, depth = queue.pop(0)
            if depth > 0:
                if node not in sums:
                    sums[node] = depth
                    sum = sum + depth
                else:
                    sum = sum - sums[node] + depth
                    sums[node] = depth
            for neighbour in graph[node]:
                queue.append((neighbour, depth+1))
        return sum


class TestSolution(unittest.TestCase):   
    def test_1(self):
        ratings = [1,0,2]
        correct_answer = 5
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)
 
    def test_2(self):
        ratings = [1,2,2]
        correct_answer = 4
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)

    def test_3(self):
        ratings = [1,3,2,2,1]
        correct_answer = 7
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)

    def test_4(self):
        ratings = [1,2,87,87,87,2,1]
        correct_answer = 13
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)


    def test_5(self):
        ratings = [1,2,7,13,13,8,9,10,8,7,5,13,14,14,8]
        correct_answer = 33
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)

    def test_6(self):
        ratings = [1,2,7,13,14,13,8,9,10,8,7,5,14,15,13,14,14,7,8,5,2]
        correct_answer = 47
        solution = Solution()
        self.assertEqual(solution.candy(ratings), correct_answer)
        
        
unittest.main()