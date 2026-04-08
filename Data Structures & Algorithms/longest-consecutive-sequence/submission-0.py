class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        tmp = sorted(list(set(nums)))
        new: int = 0
        i = 0
        while i < len(tmp):
            count = 1
            while i + 1 < len(tmp) and tmp[i] == tmp[i+1] - 1:
                count += 1
                i += 1
            if new < count:
                new = count
            i += 1
        return new
