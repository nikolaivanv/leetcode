import unittest

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        results = []
        l = 0
        k = 0
        for i in range(len(num2)-1,-1,-1):
            carryover = 0
            result = ''
            for j in range(len(num1)-1,-1,-1):
                n1 = int(num1[j])
                n2 = int(num2[i])
                r = n1 * n2 + carryover
                carryover = r // 10
                result = str(r % 10) + result
            if carryover > 0:
                result = str(carryover) + result
            result = result + ''.join(['0']*k)
            if len(result) > l:
                l = len(result)
            k = k + 1
            results.append(result)

        for i in range(len(results)):
            results[i] = results[i].rjust(l,'0')


        result = ""
        carryover = 0
        for i in range(l):
            r = 0
            for s in results:
                r = r + int(s[-i-1])
            r = r + carryover
            carryover = r // 10
            result = str(r % 10) + result
        if carryover > 0:
            result = str(carryover) + result

        return result
        

class TestSolution(unittest.TestCase):   
    def test_1(self):
        num1 = "2"
        num2 = "3"
        correct_answer = '6'
        solution = Solution()
        self.assertEqual(solution.multiply(num1, num2), correct_answer)

    def test_2(self):
        num1 = "123"
        num2 = "456"
        correct_answer = '56088'
        solution = Solution()
        self.assertEqual(solution.multiply(num1, num2), correct_answer)

    def test_3(self):
        num1 = "9"
        num2 = "9"
        correct_answer = '81'
        solution = Solution()
        self.assertEqual(solution.multiply(num1, num2), correct_answer)

    def test_3(self):
        num1 = "9133"
        num2 = "0"
        correct_answer = '0'
        solution = Solution()
        self.assertEqual(solution.multiply(num1, num2), correct_answer)

unittest.main()

