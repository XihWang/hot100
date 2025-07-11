# # Definition for singly-linked list.
# from typing import List
# import heapq
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# #     def __lt__(self, other):  # 在这里修改lt是不对的 因为改变不了系统里默认的结果
#                                 # 如果在自己ide里这养修改是没有问题的
# #         return self.val < other.val
# ListNode.__lt__ = lambda a,b: a.val < b.val
# # ListNode.__gt__ = lambda a,b: a.val > b.val 二选一都可以的
#
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         h = [head for head in lists if head]
#         heapq.heapify(h)
#         while h:
#             q = heapq.heappop(h)
#             cur.next = q
#             cur = cur.next
#             if q.next:
#                 heapq.heappush(h, q.next)
#         return dummy.next

# Definition for singly-linked list.
from typing import List


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __lt__(self, other):  # 在这里修改lt是不对的 因为改变不了系统里默认的结果
# 如果在自己ide里这养修改是没有问题的
#         return self.val < other.val


class Solution:
    def mergetwoLists(self, list1, list2):
        cur = dummy = ListNode()
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 if p1 else p2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        left = self.mergeKLists(lists[:n // 2])
        right = self.mergeKLists(lists[n // 2:])
        return self.mergetwoLists(left, right)












