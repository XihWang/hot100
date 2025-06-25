# 自己的方法
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         output = []
#         ls_dc=[]
#         for string in strs:
#             keys = set(string)
#             dc = {}
#             for i in keys:
#                 dc[i] = 0
#             for char in string:
#                 dc[char] += 1
#             ls_dc.append(dc)
#
#
#         for i in range(len(ls_dc)):
#             lt = []
#             if ls_dc[i] is not None:
#                 lt.append(i)
#             else:
#                 continue
#             for j in range(i+1, len(ls_dc)):
#                 if ls_dc[i] == ls_dc[j]:
#                     lt.append(j)
#             for idx in lt:
#                 ls_dc[idx] = None
#
#             output.append([strs[idx] for idx in lt])
#         return output

# 官方解法 用defaultdict 来直接对list append
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dc = defaultdict(list)
        for string in strs:
            newstring = sorted(string)
            key = "".join(newstring)
            dc[key].append(string)
        return list(dc.values())



if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
