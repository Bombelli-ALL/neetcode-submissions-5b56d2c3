class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret: list[int] = []
        t = 1
        bol = 0
        for e in nums:
            if e != 0:
                t *= e
            elif bol == 0:
                bol =  1
            else:
                bol = 2
        for e in nums:
            if bol == 0:
                ret.append(t // e)
            elif bol == 2:
                return [0] * len(nums)
            else:
                if e == 0:
                    ret.append(t)
                else:
                    ret.append(0)
        return ret