class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty())
            return 0;
        int l = 0;
        int r = height.size() - 1 ;
        int left_max = height[l];
        int right_max = height[r];
        int resulte = 0;
        while (l < r) {
            if (left_max < right_max){
                l++;
                left_max = max(left_max, height[l]);
                resulte += left_max - height[l];
            }
            else
            {
                r--;
                right_max = max(right_max, height[r]);
                resulte += right_max - height[r];
            }
        }
        return resulte;
        
    }
};
