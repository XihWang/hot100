class Node:
    __slots__ = 'prev', 'next', 'key', 'value'
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value

class LRUCache:
    # 双向链表主要是为了删除超过容量的那个最久没有用到的关键字（dummy.prev）
    # 哈希表形成关键字和node的对应 方便对node处理
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.push_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.push_front(node)
            node.value = value
        else:
            self.key_to_node[key] = node = Node(key, value)
            self.push_front(node)
            if len(self.key_to_node) > self.capacity:
                x = self.dummy.prev
                self.remove(x)
                del self.key_to_node[x.key]



    # def get_node(self, key):
    #     if key not in self.key_to_node:
    #         return None
    #     else:
    #         node = self.key_to_node[key]
    #         self.remove(node)
    #         self.push_front(node)
    #         return node



    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def push_front(self, node):
        self.dummy.next.prev = node
        node.next = self.dummy.next
        self.dummy.next = node
        node.prev = self.dummy


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)