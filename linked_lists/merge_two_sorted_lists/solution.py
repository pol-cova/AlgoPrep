from typing import Optional
from linked_lists.linked_list.node import Node

class MergeTwoSortedListsSolution:
    def merge_two_lists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        current = dummy
        
        while list1 is not None and list2 is not None:
            if list1.value <= list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        if list1 is None:
            self._append_list(current, list2)
        else:
            self._append_list(current, list1)
            
        return dummy.next

    def _append_list(self, current: Node, list_to_append: Optional[Node]) -> None:
        while list_to_append is not None:
            current.next = list_to_append
            list_to_append = list_to_append.next
            current = current.next
