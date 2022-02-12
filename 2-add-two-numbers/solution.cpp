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
// O(m+n) time | O(max(m,n)) space
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *sum_list = new ListNode();
        ListNode *cur = sum_list;
        
        int carry = 0;
        while (l1 || l2 || carry){
            int digit1 = (l1) ? l1->val : 0;
            int digit2 = (l2) ? l2->val : 0;
                
            // add digits
            int result = digit1 + digit2 + carry;
            carry = result / 10;
            result = result % 10;
            cur->next = new ListNode(result);
            
            // update pointers
            cur = cur->next;
            l1 = (l1) ? l1->next : NULL;
            l2 = (l2) ? l2->next : NULL;
        }
        return sum_list->next;
    }
};
