# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 主要是要让长度相同 这样遍历才会找到对应的位置 注意是结点相同 也就是地址相同 而不是val相同
        # 方法一 减去长度法
        # p1, p11 = headA, headA
        # p2, p22 = headB, headB
        # lenA = 0
        # lenB = 0
        # while p1 != None:
        #     p1 = p1.next
        #     lenA += 1
        #
        # while p2 != None:
        #     p2 = p2.next
        #     lenB += 1
        # n = abs(lenA - lenB)
        # if lenA > lenB:
        #     for i in range(n):
        #         p11 = p11.next
        # else:
        #     for i in range(n):
        #         p22 = p22.next
        # while p11 != None:
        #     if p11 == p22:
        #         return p11
        #     p11 = p11.next
        #     p22 = p22.next
        # return None

        # 方法二 链接
        p1, p2 = headA, headB

        # 当 p1 和 p2 不相等时继续遍历
        # 如果将代码改为 p1.next = headB，会导致链表 A 的末尾直接连接到链表 B 的头部，从而形成一个循环链表。在这种情况下，指针 p1 和 p2 都会在链表 A 和链表 B 之间无限循环，无法跳出循环条件 while p1 != p2，最终导致死循环。
        # 原代码中使用了 p1 = p1.next if p1 else headB，这里的逻辑是当 p1 到达链表 A 的末尾时，将其重置为链表 B 的头部，而不是修改链表结构。因此不会形成死循环。
        while p1 != p2:
            # 如果 p1 到达链表 A 的末尾，则切换到链表 B 的头部
            p1 = p1.next if p1 else headB
            # 如果 p2 到达链表 B 的末尾，则切换到链表 A 的头部
            p2 = p2.next if p2 else headA

        # 最终 p1 和 p2 要么同时为 None（无交点），要么指向交点
        return p1



