# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        response = None
        left = l1
        right = l2
                    
                    
        def insertNode(x: int):
            
            nonlocal response
            current = response
            newNode = ListNode(x)
            
            
            if response == None:
                response = ListNode(x)
                return
            
            while (current.next):
                current = current.next
                
            #When next == None, assign next to new list node 
            current.next = ListNode(x)
        
        
        
        while left or right:
            
            if left and right:
                if right.val < left.val:
                    insertNode(right.val)                    
                    right = right.next
                    continue
                
                insertNode(left.val)    
                left = left.next
                continue
                
                
            if left:
                insertNode(left.val)
                left = left.next

            if right:
                insertNode(right.val)
                right = right.next

        
        return response