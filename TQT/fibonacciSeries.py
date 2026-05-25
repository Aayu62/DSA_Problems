class Solution:
    def fibonacci(self, n: int) -> list:
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

if __name__ == "__main__":
    sol = Solution()
    terms = int(input())
    print(sol.fibonacci(terms))