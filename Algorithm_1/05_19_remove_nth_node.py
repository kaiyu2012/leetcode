# 19. Remove Nth Node From End of List

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        
        new_list = head    
        lead = head
        before_nth = head
        if lead.next:
            nth = lead.next
        else:
            return lead.next
        
        carry = 0      
        while lead:
            lead  = lead.next
            carry += 1
            if carry > n+1:
                nth = nth.next
                before_nth = before_nth.next
                
        before_nth.next = nth.next  
        
        return new_list
            
            
            
# test 
def main():
    # l1 = [1,2,3,4,5,6,7,8]
    # l1 = [1,2,3,4,5]
    l1 = [1]
    lx = ListNode(l1[0])
    head = lx
    for i in range(1, len(l1)):
        lx.next = ListNode(l1[i])
        lx = lx.next
    
    
    s = Solution
    new_list = s.removeNthFromEnd(s, head, 1)
    
    x = new_list
    while x:
        print(x.val)
        x=x.next
           
                    
if __name__ == "__main__":
    main()
