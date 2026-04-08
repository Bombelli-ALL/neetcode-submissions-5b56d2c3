class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cal: dict[int: int] = {}
        while nums:
            tmp = [x for x in nums if x == nums[0]]
            cal.update({nums[0]: len(tmp)})
            nums = [item for item in nums if item not in tmp]
        new = sorted(cal.items(), key= lambda x: x[1])
        last = [x[0] for x in new]
        return last[-k:]
