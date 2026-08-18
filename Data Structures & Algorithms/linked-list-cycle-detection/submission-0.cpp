/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode *tmp;
        vector<ListNode * > arr;
        tmp = head;
        while (tmp != nullptr){
            if (std::ranges::contains(arr, tmp))
                return true;
            arr.push_back(tmp);
            tmp = tmp->next;
        }
        return false;
    }
};
