import sys
sys.set_int_max_str_digits(1000000)

print(sys.get_int_max_str_digits())

class Solution:
    def factorialOf(self, num: int) -> int:
        if num <= 1:
            return 1
        fact = 1
        for i in range(1, num+1):
            fact *= (i)
        return fact
    
class main:
    N = int(input())
    obj = Solution()
    print(f"Factorial of {N} : {obj.factorialOf(N):.5e}")