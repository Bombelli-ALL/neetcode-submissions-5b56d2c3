class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, r = 0, len(nums) - 1
        while a <= r:
            m = (a + r) // 2
            if nums[m] == target:
                return m
            if nums[a] <= nums[m]:
                if target > nums[m] or target < nums[a]:
                    a = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    a = m + 1 

        return -1
