# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                p.next = p1
                # p1 = p1.next
                p = p.next
                temp = p1
                p1 = temp.next
                temp.next = None
            else:
                p.next = p2
                # p2 = p2.next   这里交换和直接next都可以的   86题分割的时候就不能next
                p = p.next
                temp = p2
                p2 = temp.next
                temp.next = None

        if p1 == None:
            p.next = p2
        else:
            p.next = p1
        return dummy.next

# 方法二 用最小堆
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ListNode.__lt__ = lambda a,b: a.val < b.val
# import heapq
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = cur = ListNode()
#         h = [list1, list2]
#         if list1 and list2:
#             heapq.heapify(h)
#         elif list1 and not list2:
#             return list1
#         elif list2 and not list1:
#             return list2
#         else:
#             return
#         while h:
#             q = heapq.heappop(h)
#             cur.next = q
#             cur = cur.next
#             if q.next:
#                 heapq.heappush(h, q.next)
#         return dummy.next

