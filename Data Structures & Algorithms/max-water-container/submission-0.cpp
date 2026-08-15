class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0;
        int j = heights.size() - 1;
        int max = 0;
        int area;
        while (i < j){
            area = min(heights[i], heights[j]) * (j - i);
            if (area > max)
                max = area;
            if (heights[i] > heights[j])
                j -= 1;
            else
                i += 1;
        }
        return max;
    }
};
