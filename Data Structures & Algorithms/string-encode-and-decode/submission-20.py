class Solution:

    def encode(self, strs: List[str]) -> str:
        ret: str = ''
        n = len(strs) - 1
        for i in strs:
            ret += str(len(i)) + "#" + i
        return ret

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lene = int(s[i:j])
            res.append(s[j + 1 : j + 1 + lene])
            i = j + 1+ lene
        return res
