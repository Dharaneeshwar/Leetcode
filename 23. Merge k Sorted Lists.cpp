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
        struct compare {
            bool operator()(const ListNode* l, const ListNode* r) {
                return l->val > r->val;
            }
        };
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            ListNode* head = new ListNode();
            ListNode* last = head;
            priority_queue<ListNode*,vector<ListNode*>,compare> pq;
            for (int i=0;i<lists.size();i++){
                if (lists[i] != nullptr)
                {
                    pq.push(lists[i]);
                    lists[i] = lists[i]->next;
                }
            }
            while (pq.size()){
                ListNode* temp = pq.top();
                pq.pop();
                last->next = new ListNode(temp->val);
                last = last->next; 
                if (temp->next)
                    pq.push(temp->next);
            }
            return head->next;
        }
        
    };