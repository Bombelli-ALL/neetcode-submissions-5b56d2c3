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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *tmp = head;
        int size = 0;
        while(tmp){
            tmp = tmp->next;
            size++;
        }
        ListNode dummy(0);         // fix: dummy node handles "remove head" case
        dummy.next = head;
        tmp = &dummy;

        for (int i = 0; i < size - n; i++)   // walk to node just before target
            tmp = tmp->next;

        ListNode *delet = tmp->next;
        tmp->next = tmp->next->next;
        delete delet;

        return dummy.next; 
    }
};
