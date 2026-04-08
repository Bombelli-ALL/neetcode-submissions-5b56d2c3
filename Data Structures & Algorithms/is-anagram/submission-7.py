class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        new: list = [x for x in t]
        for i in s:
            if i in new:
                new.remove(i)
                continue
            else:
                return False
        return True