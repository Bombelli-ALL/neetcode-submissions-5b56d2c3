class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> charset;
        int res = 0;
        int j = 0;

        for (int  i = 0; i < s.length(); i++) {
            while (charset.contains(s[i]) ){
                charset.erase(s[j]);
                j++;
            }
            charset.insert(s[i]);
            res = max(res, i - j + 1);
        }
        return res;
    }
};
