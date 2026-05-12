class Trie:

    # 定义内部节点类
    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.is_end = False
            self.is_pre = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            cur = ord(c) - ord('a')
            if not p.children[cur]:
                p.children[cur] = self.Node()
            p = p.children[cur]
            p.is_pre = True

        p.is_end = True

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            u = ord(c) - ord('a')
            if not p.children[u]:
                return False
            p = p.children[u]

        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            u = ord(c) - ord('a')
            if not p.children[u]:
                return False
            p = p.children[u]

        return p.is_pre

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)