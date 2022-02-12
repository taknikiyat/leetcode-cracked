/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// O(m+n) time | O(max(m,n)) space
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum_list = new ListNode();
        ListNode cur = sum_list;
        
        int carry = 0;
        while (l1!=null || l2!=null || carry>0){
            int digit1 = (l1!=null) ? l1.val : 0;
            int digit2 = (l2!=null) ? l2.val : 0;
                
            // add digits
            int result = digit1 + digit2 + carry;
            carry = result / 10;
            result = result % 10;
            cur.next = new ListNode(result);
            
            // update pointers
            cur = cur.next;
            l1 = (l1!=null) ? l1.next : null;
            l2 = (l2!=null) ? l2.next : null;
        }
        return sum_list.next;        
    }
}
