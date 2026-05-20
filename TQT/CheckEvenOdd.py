class Solution:
    def checkEven(self, num: int) -> bool :
        return num%2==0 
    
class main:
    num = int(input())
    obj = Solution()
    print(f"Number {num} is:", "Even" if obj.checkEven(num) else "Odd")