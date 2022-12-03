class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        if nums[pivot] > target:
            return pivot
        else:
            return pivot + 1


    def mergesort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            mergesort(L)
            mergesort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    k += 1
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    k += 1
            while i < len(L):
                arr[k] = L[i]
                k += 1
                i += 1
            while j < len(R):
                arr[k] = R[j]
                k += 1
                j += 1

