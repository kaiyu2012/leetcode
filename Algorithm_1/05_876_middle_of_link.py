# 876. Middle of the Linked List

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        lead = head

        middle = lead
        carry = False
        
        while lead:
            lead  = lead.next
            if lead:
                print(f'lead - {lead.val}')
            if carry:
                middle = middle.next
                print(f'   middle - {middle.val}')            
            carry = not carry
            
        return middle
            
            
            
# test 
def main():
    # l1 = [1,2,3,4,5,6,7,8]
    l1 = [1,2,3,4,5]
    
    lx = ListNode(l1[0])
    head = lx
    for i in range(1, len(l1)):
        lx.next = ListNode(l1[i])
        lx = lx.next
    
    
    s = Solution
    x = s.middleNode(s, head)
    
    print(x.val)
        
                    
if __name__ == "__main__":
    main()
