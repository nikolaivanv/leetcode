import unittest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        k = 1
        r = 1
        for i in range(1,l):
            if nums[i] != nums[i-1]:
                r = 1
                nums[k] = nums[i]
                k = k + 1
            else:
                r = r + 1
                if r < 3:
                    nums[k] = nums[i]
                    k = k + 1
        return k
    #print(nums, f"i={i+1}", f"k={k}", f"r={r}")
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,1,1,2,2,3]
        
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=1 k=1 r=1
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=2 k=2 r=2
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=3 k=3 r=1
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=4 k=4 r=2
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=5 k=4 r=3
        # [0, 0, 1, 1, 1, 1, 2, 3, 3] i=6 k=4 r=4
        # [0, 0, 1, 1, 2, 1, 2, 3, 3] i=7 k=5 r=1
        # [0, 0, 1, 1, 2, 3, 2, 3, 3] i=8 k=6 r=1
        # [0, 0, 1, 1, 2, 3, 2, 3, 3] i=9 k=7 r=2
        
        solution = Solution()
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1,1,2,2,3])
    
    def test_2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        solution = Solution()
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0,0,1,1,2,3,3])
    
unittest.main()