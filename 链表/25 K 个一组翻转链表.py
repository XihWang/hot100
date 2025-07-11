# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        dummy = ListNode(next = head)
        p = dummy
        # cur = head
        # pre = None
        # while n >= k:
        #   n -= k  # 可以替换下面二行
        times = n//k
        for _ in range(times):
            # p是cur前一个元素
            # cur是要替换的第一个元素 pre是cur是左边的元素
            # 最后是pre在最后一个要替换的元素 cur在pre右边一个元素
            cur = p.next
            pre = None
            for _ in range(k): # 有几个元素就要循环几次
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            tmp = p.next
            p.next.next = cur
            p.next = pre
            p = tmp
        return dummy.next