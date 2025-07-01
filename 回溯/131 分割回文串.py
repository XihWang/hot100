class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        trace = []
        def backtrace(start):
            if start == n:  # 注意这里和子集问题的不同，要等到长度到了才能append 不能够省略
                res.append(trace[:])
                return
            for i in range(start, n):
                t = s[start: i + 1] # 注意这里要＋1 因为0：0 取出来是空字符串
                if t[:] == t[::-1]:
                    trace.append(t)
                    backtrace(i + 1)
                    trace.pop()
        backtrace(0)
        return res