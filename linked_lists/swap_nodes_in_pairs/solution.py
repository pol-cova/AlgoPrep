from typing import Optional
from linked_lists.linked_list.node import Node

class SwapNodesInPairsSolution:
    def swap_nodes_in_pairs(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head
            
        remaining = head.next.next
        
        # Swap
        first = head
        second = head.next
        
        second.next = first
        first.next = self.swap_nodes_in_pairs(remaining)
        
        return second
