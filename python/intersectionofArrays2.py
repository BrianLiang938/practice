class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for x in range(len(nums1)):
            for y in range(len(nums2)):
                if nums1[x] == nums2[y]:
                    output.append(nums1[x])
                    nums2.remove(nums2[y])
                    y -= 1
                    break
        return output
