# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # global ans 如果下面要用global 那么上面的也必须变成全局变量
        # 如果上面没有global就还是pathSum的局部变量 若此时下面有global 一个是全局 一个是局部 还是改不了
        # 所以要两个都global才能都改
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        def dfs(root, s):
            if not root:
                return
            s += root.val
            # global ans 需要上面也变成global
            nonlocal ans
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(root.left, s)
            dfs(root.right, s)
            cnt[s] -= 1
    # 想一想，恢复现场恢复的是什么？是去掉当前节点的信息。递归右子树的时候需不需要当前节点的信息？需要。所以要在递归完右子树后，才能恢复现场。
        dfs(root, 0)
        return ans

# 问：为什么递归参数 s 不需要恢复现场？

# 答：s 是基本类型，在函数调用的时候会复制一份往下传递，s += node.val 修改的仅仅是当前递归函数中的 s 参数，并不会影响到其他递归函数中的 s。注：如果把 s 放在递归函数外，此时只有一个 s，执行 s += node.val 就会影响全局了。

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/path-sum-iii/solutions/2784856/zuo-fa-he-560-ti-shi-yi-yang-de-pythonja-fmzo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
