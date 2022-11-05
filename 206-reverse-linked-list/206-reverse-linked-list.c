/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* cur=head;
    struct ListNode* prev=NULL;
    struct ListNode* nextn=NULL;
    while(cur!=NULL){
        nextn=cur->next;
        cur->next=prev;
        prev=cur;
        cur=nextn;
    }
    return prev;
}