class Solution:
    def isHappy(self, n: int) -> bool:
        list = [n]
        sum = 0
        while n >= 1:
            temp = n % 10
            n = n // 10
            sum += temp * temp
        if sum == 1:
            return 1
        list.append(sum)
        slow = 0
        fast = 1
        while list[slow] != list[fast]:
            n = list[-1]
            sum = 0
            while n >= 1:
                temp = n % 10
                n = n // 10
                sum += temp * temp
            if sum == 1:
                return 1
            list.append(sum)
            n = sum
            sum = 0
            while n >= 1:
                temp = n % 10
                n = n // 10
                sum += temp * temp
            if sum == 1:
                return 1
            list.append(sum)
            slow += 1
            fast += 2
        return 0