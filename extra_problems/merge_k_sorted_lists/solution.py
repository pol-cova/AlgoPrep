from typing import List, Optional
from extra_problems.merge_k_sorted_lists.node import Node

class MergeKSortedListsSolution:
    def merge_k_lists(self, lists: List[Optional[Node]]) -> Optional[Node]:
        if not lists:
            return None

        # Work on a copy of the list of heads to avoid modifying the input parameter in-place
        lists_copy = list(lists)
        offset = 1
        n = len(lists_copy)
        while offset < n:
            for i in range(0, n - offset, offset * 2):
                lists_copy[i] = self.merge_two_lists(lists_copy[i], lists_copy[i + offset])
            offset *= 2

        return lists_copy[0] if n > 0 else None

    def merge_two_lists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        dummy = Node(-2147483648)
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
