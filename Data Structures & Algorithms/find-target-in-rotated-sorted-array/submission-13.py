class Solution():
    def search(self, nums: List[int], target: int) -> int:
        a, r = 0, len(nums) - 1
        while a <= r:
            m = (a + r) // 2
            if nums[m] == target:
                return m 
            elif nums[a] <= nums[m]:
                if nums[a] <= target < nums[m]:
                    r = m - 1
                else:
                    a = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    a = m + 1
                else:
                    r = m - 1
        return -1