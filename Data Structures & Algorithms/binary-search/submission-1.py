class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, r = 0, len(nums) - 1
        while a <= r:
            m = a  + ((r - a) // 2)
            if nums[m] > target:
                r = m - 1 
            elif nums[m] < target:
                a = m + 1
            else:
                return m
        return -1
