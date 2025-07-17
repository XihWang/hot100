# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
    def mid(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 反转链表与原来进行比较  最终是错误的
        # 注意直接反转整一个链表 就不能原本的链表比较了 因为原本的链表已经变了
        # 所以这个方法是不对的
        # pre = None
        # cur = head
        # ls = []
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # while pre:
        #     if head.val == pre.val:
        #         pre = pre.next
        #         head = head.next
        #     else:
        #         return False
        # return True

        # 法二 用列表的reverse
        # ls = []
        # while head:
        #     ls.append(head.val)
        #     head = head.next
        # lt = ls[:]
        # ls.reverse()
        # if ls == lt:
        #     return True
        # else:
        #     return False

        # 法三  中点+倒序
        mid = self.mid(head)
        head2 = self.reverse(mid)
        while head2:
            if head2.val != head.val:
                return False
            head2 = head2.next
            head = head.next
        return True





