from ch04_LinkedLists._00_linkedlist.node import Node

class RemoveDupsSolution:
    def remove_dups(self, head: Node) -> None:
        if not head:
            return
        seen = {head.value}
        current = head
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.value)
                current = current.next
