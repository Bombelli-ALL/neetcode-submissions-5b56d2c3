class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new: list[int] = []
        for ele in nums:
            if ele not in new:
                new.append(ele)
            else:
                return True
        return False