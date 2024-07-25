import unittest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)
        m = nums[0]
        votes = 1
        for i in range(1, l):
            if nums[i] == m:
                votes = votes + 1
            else:
                votes = votes - 1
                if votes == 0:
                    m = nums[i]
                    votes = 1
        return m
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [3,2,3]
        solution = Solution()
        m = solution.majorityElement(nums)
        self.assertEqual(m, 3)
    
    def test_2(self):
        nums = [2,2,1,1,1,2,2]
        solution = Solution()
        m = solution.majorityElement(nums)
        self.assertEqual(m, 2)
    
unittest.main()