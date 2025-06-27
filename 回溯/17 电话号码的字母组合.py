class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAP = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        res = []
        path = [''] * n
        if n == 0:
            return []
        def backtrace(length):
            if length == n:
                res.append(''.join(path))
                return
            for c in MAP[int(digits[length])]:
                path[length] = c
                backtrace(length + 1)
        backtrace(0)
        return res

