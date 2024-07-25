import unittest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        k = 1
        for i in range(1,l):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k = k + 1
        return k
    
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 5, 9, 9, 11]
        k = 1
        # [0, 1, 2, 3, 4, 5]
        # [1, 1, 5, 9, 9, 11]
        # duplicates = [1, 4]
        # unique = [0, 2, 3, 5]
        # 
        # [1, 1, 5, 9, 9, 11] | i = 0 | k = 0
        # [1, 1, 5, 9, 9, 11] | i = 1 | k = 0
        # [1, 5, 5, 9, 9, 11] | i = 2 | k = 1
        # [1, 5, 5, 9, 9, 11] | i = 3 | k = 1
        # [1, 5, 9, 9, 9, 11] | i = 4 | k = 2
        # [1, 5, 9, 9, 9, 11] | i = 5 | k = 2
        # [1, 5, 9, 9, 9, 11] | i = 6 | k = 2
        # [1, 5, 9, 11, 9, 11] | i = 6 | k = 3
        
        solution = Solution()
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 5, 9, 11])
    
    def test_2(self):
        nums = [1,1,2]
        k = 2
        solution = Solution()
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
unittest.main()