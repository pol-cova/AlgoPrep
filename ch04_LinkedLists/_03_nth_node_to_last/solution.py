from typing import Optional
from ch04_LinkedLists._00_linkedlist.node import Node

class NthNodeToLastSolution:
    def nth_node_to_last(self, head: Optional[Node], n: int) -> Optional[Node]:
        p1 = head
        p2 = head
        
        for _ in range(n):
            if p1 is None:
                return None
            p1 = p1.next
            
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
            
        return p2
