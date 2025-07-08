# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
    # 法一 直接遍历
    #     count = 0
    #     p_count = head
    #     dummy = ListNode(-1)
    #     p = dummy
    #     p.next = head
    #     while p_count != None:
    #         p_count = p_count.next
    #         count += 1
    #     for i in range(count-n):
    #         p = p.next
    #     temp = p.next
    #     p.next = temp.next
    #     temp.next = None
    #
    #     return dummy.next
    # 法二  双指针 减少一次遍历

        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

