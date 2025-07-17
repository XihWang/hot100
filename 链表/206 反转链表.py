# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 方法一 对val进行操作 然后用容器进行反转
        # p,q = head,head
        # ls = []
        # while p:
        #     ls.append(p.val)
        #     p = p.next
        # ls.reverse()
        # for i in ls:
        #     q.val = i
        #     q = q.next
        # return head

        # 方法二 双指针迭代
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

