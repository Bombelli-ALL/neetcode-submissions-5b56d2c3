import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a, r = 1, max(piles)
        res = r
        while a <= r:
            hour = 0
            n = (r + a) // 2
            for e in piles:
                hour += math.ceil(e / n)
            if hour > h:
                a = n + 1
            elif hour <= h:
                res = min(res, n)
                r = n - 1
        return res

