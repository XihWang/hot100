# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 速度太慢了
        # p1,p2 = l1,l2
        # while p1 and p2:
        #     if p1.next is None and p2.next is not None:
        #         p1.next = ListNode(0)
        #     if p2.next is None and p1.next is not None:
        #         p2.next = ListNode(0)
        #     p1 = p1.next
        #     p2 = p2.next
        #
        # dummy = ListNode(-1)
        # p = dummy
        # flag = 0
        # while l1 and l2:
        #     if flag == 0:
        #         num = l1.val + l2.val
        #     else:
        #         num = l1.val + l2.val + 1
        #         flag = 0
        #     if num >= 10:
        #         num = num - 10
        #         flag = 1
        #
        #     p.next = ListNode(num)
        #     p = p.next
        #     l1 = l1.next
        #     l2 = l2.next
        # if flag == 1:
        #     p.next = ListNode(1)
        # return dummy.next

        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1:
                carry += l1.val  # 节点值和进位加在一起
                l1 = l1.next  # 下一个节点
            if l2:
                carry += l2.val  # 节点值和进位加在一起
                l2 = l2.next  # 下一个节点
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点




