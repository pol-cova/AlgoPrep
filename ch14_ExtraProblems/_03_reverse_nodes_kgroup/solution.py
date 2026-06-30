from typing import Optional
from ch14_ExtraProblems._03_reverse_nodes_kgroup.list_node import ListNode

class ReverseNodesKGroupSolution:
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        root = ListNode(-1)
        root.next = head
        current = head
        prev = root

        while current is not None:
            tail = current
            nodes_to_advance = k

            while current is not None and nodes_to_advance > 0:
                current = current.next
                nodes_to_advance -= 1

            if nodes_to_advance > 0:
                prev.next = tail
            else:
                prev.next = self._reverse(tail, k)
                prev = tail

        return root.next

    def _reverse(self, head: ListNode, k: int) -> ListNode:
        prev = None
        current = head
        
        while current is not None and k > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            k -= 1
            
        return prev
