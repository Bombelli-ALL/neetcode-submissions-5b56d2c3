class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int target_matche;
        int i = 0;
        int j =  numbers.size()  - 1;
        vector<int> resulte;
        while (i < j) {
            target_matche = numbers[i] + numbers[j];
            if (target_matche > target)
                j -= 1;
            else if (target_matche < target)
                i += 1;
            else
            {
                resulte.push_back(i + 1);
                resulte.push_back(j + 1);
                return resulte;
            }
        }
        return resulte;
    }
};
