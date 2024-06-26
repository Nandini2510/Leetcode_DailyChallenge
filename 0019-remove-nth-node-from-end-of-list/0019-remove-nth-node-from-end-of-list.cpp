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
        int num = 0;
        ListNode* temp = head;
        while(temp != NULL){
            temp = temp->next;
            num++;
        }
        temp = head;
        int i = 0;
    
        while(i < num - n - 1){
            temp = temp->next;
            i++;
        }
        if(num - n == 0){
            return head->next;
        }
        if(temp->next == NULL){
            temp->next = NULL;
        }
        temp->next = temp->next->next;
        return head;
    }
};