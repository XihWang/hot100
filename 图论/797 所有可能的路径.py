# class Solution(object):
#  回溯法
#     def allPathsSourceTarget(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         res = []
#         trace =[]
#         n = len(graph)
#         # visit = [False] * n
#         def backtrace(nodes):
#             for node in nodes:
#                 # if visit[node]:
#                 #     continue
#                 trace.append(node)
#                 # visit[node] = True
#                 if trace[-1] == n - 1:
#                     res.append(trace[:])
#                 backtrace(graph[node])
#                 trace.pop()
#                 # visit[node] = False

#         backtrace([0])
#         return res

# DFS
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)

        # @lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return [[n - 1]]
            ans = []
            for nxt in graph[node]:
                for res in dfs(nxt):
                    ans.append([node] + res)
            return ans

        return dfs(0)
