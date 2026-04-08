class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new: list = [x for x in t]
        for i in s:
            if i in new:
                new.remove(i)
                continue
            else:
                return False
        if new :
            return False
        return True