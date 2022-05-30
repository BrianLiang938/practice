class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for m in range(1, n + 1):
            if m % 15 == 0:
                output.append("FizzBuzz")
            elif m % 3 == 0:
                output.append("Fizz")
            elif m % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(m))
        return output