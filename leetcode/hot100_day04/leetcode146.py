class LRUCache:

    # 146 LRU 缓存：本质上就是将所有结点维护成一个双链表
    class Node:
        def __init__(self, key, val, pre=None, next=None):
            self.key = key
            self.val = val
            self.pre = pre
            self.next = next

    class DoubleLinkedList:
        def __init__(self):
            self.head = LRUCache.Node(0, 0)
            self.tail = LRUCache.Node(0, 0)
            self.head.next = self.tail
            self.tail.pre = self.head

        def add_node_right(self, cur, node):
            node.next = cur.next
            node.pre = cur
            cur.next.pre = node
            cur.next = node

        def remove_cur(self, cur):
            cur.next.pre = cur.pre
            cur.pre.next = cur.next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.doubleList = LRUCache.DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            # 将当前结点从链表删除，在插入到最左边
            cur = self.cache[key]
            self.doubleList.remove_cur(cur)
            self.doubleList.add_node_right(self.doubleList.head, cur)
            return cur.val
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 创建一个结点
            node = LRUCache.Node(key, value)
            # 加入到缓存中
            self.cache[key] = node
            # 加入到链表中
            self.doubleList.add_node_right(self.doubleList.head, node)
            if len(self.cache) > self.capacity:
                # 从链表删除最右边的结点
                del_node = self.doubleList.tail.pre
                self.doubleList.remove_cur(del_node)
                # 删除缓存
                del self.cache[del_node.key]

        else:
            # 覆盖值，跟新它在链表中的位置
            node = self.cache[key]
            node.val = value

            self.doubleList.remove_cur(node)
            self.doubleList.add_node_right(self.doubleList.head, node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)