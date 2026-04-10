class Solution:
    def findMin(self, nums: List[int]) -> int:
        a, r = 1, len(nums) - 1
        res = nums[0]
        while a <= r:
            if nums[a] < nums[r]:
                res = min(res, nums[a])
                break
            m = (r + a) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[a]:
                a = m + 1
            else:
                r = m - 1
        return res
            
