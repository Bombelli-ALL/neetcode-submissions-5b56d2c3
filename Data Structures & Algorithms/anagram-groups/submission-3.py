class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def ar(s: str, t: str) -> bool:
            if len(s) != len(t):
	            return False
            tmp = [x for x in t]
            for i in s:
                if i in tmp:
                    tmp.remove(i)
                    continue
                else:
                    return False
            return True
        ret: list[list[str]] = []
        while strs:
            sep = filter(lambda x: ar(strs[0], x), strs)
            dg = list(sep)
            ret.append(dg)
            strs = [item for item in strs if item not in dg]
        return ret



