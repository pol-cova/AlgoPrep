from typing import Optional
from linked_lists.linked_list.node import Node

class AddTwoNumbersSolution:
    def add_two_numbers(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        result = Node(-1)
        current = result
        carry = 0
        
        while list1 is not None or list2 is not None:
            current.next = Node(-1)
            current = current.next
            
            digit = carry
            if list1 is not None:
                digit += list1.value
                list1 = list1.next
            if list2 is not None:
                digit += list2.value
                list2 = list2.next
                
            carry = digit // 10
            digit = digit % 10
            current.value = digit
            
        if carry > 0:
            current.next = Node(carry)
            
        return result.next
