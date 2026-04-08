class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s))
        st.strip()
        n = st.lower()
        d = n[::-1]
        if d == n:
            return True
        return False
