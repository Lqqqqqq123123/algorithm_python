class Node:
    def __init__(self):
        self.pre = 0
        self.son = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        p = self.root
        for c in s:
            u = ord(c) - ord('a')
            if not p.son[u]:
                p.son[u] = Node()
            p = p.son[u]

        p.pre += 1
    def query(self, s,  n):
        p = self.root
        res = 0
        for c in s:
            u = ord(c) - ord('a')
            if not p.son[u] or p.son[u].pre < n:
                return res
            else:
                res += 1
                p = p.son[u]

        return res

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        n = len(strs)
        for s in strs:
            trie.insert(s)

        return trie.query(strs[0], n)
