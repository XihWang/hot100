class Node():
    def __init__(self):
        self.son = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word):
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return 1 if cur.end else 2



    def search(self, word: str) -> bool:
        return self.find(word) == 1

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# # 最朴素的方法 时间复杂度太高 只能击败5%
# class Trie:
#
#     def __init__(self):
#         self.tire = []
#
#     def insert(self, word: str) -> None:
#         self.tire.append(word)
#
#     def search(self, word: str) -> bool:
#         return word in self.tire
#
#     def startsWith(self, prefix: str) -> bool:
#         n = len(prefix)
#         for i in self.tire:
#             if len(i) >= n and prefix == i[:n]:
#                 return True
#         return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)