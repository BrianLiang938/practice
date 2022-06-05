class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        curr = min(height[left], height[right]) * (right - left)
        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            if curr < temp:
                curr = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return curr
