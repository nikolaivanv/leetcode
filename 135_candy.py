import unittest


class Solution:
    def candy(self, ratings: list[int]) -> int:
        

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