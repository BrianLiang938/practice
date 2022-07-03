class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        out = 1
        flag = 0
        if len(nums) > 1 and nums[0] < nums[1]:
            flag = 1
        if len(nums) > 1 and nums[0] != nums[1]:
            out = 2
        else:
            flag = -1
        for i in range(1, len(nums) - 1):
            if flag == -1 and nums[i] != nums[i+1]:
                if nums[i] < nums[i+1]:
                    flag = 1
                    out += 1
                elif nums[i] > nums[i+1]:
                    flag = 0
                    out += 1
            elif flag == 0 and nums[i] < nums[i+1]:
                flag = 1
                out += 1
            elif flag == 1 and nums[i] > nums[i+1]:
                flag = 0
                out += 1
        return out