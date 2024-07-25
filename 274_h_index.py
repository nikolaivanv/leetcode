import unittest


class Solution:
    # simple solution with sorting
    # def hIndex(self, citations: list[int]) -> int:
    #     citations.sort(reverse=True)
    #     h = 0
    #     for i, c in enumerate(citations):
    #         if c > h:
    #             h = h + 1
    #         else:
    #             break
    #     return h

    def hIndex(self, citations: list[int]) -> int:
        counts = dict()
        h = 0
        for i, c in enumerate(citations):
            for j in range(h+1, c+1):
                if j in counts:
                    counts[j] = counts[j] + 1
                else:
                    counts[j] = 1
                if counts[j] == j:
                    h = j
        return h


class TestSolution(unittest.TestCase):   
    def test_1(self):
        citations = [3,0,6,1,5]
        correct_answer = 3
        solution = Solution()
        self.assertEqual(solution.hIndex(citations), correct_answer)
        
    def test_2(self):
        citations = [1,3,1]
        correct_answer = 1
        solution = Solution()
        self.assertEqual(solution.hIndex(citations), correct_answer)
   
    
unittest.main()