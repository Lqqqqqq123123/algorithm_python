from typing import List
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.val_idx = defaultdict(set)

    @property
    def n(self):
        return len(self.arr)

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        if val not in self.val_idx:
            self.val_idx[val].add(self.n - 1)
            return True
        else:
            self.val_idx[val].add(self.n - 1)
            return False

    def remove(self, val: int) -> bool:
        # 删除val
        if val not in self.val_idx:
            return False
        else:
            # 先拿到最后一个元素
            last = self.arr[-1]
            last_pos = self.n - 1
            # 随便找一个val对于的位置，同时删除它
            pos = self.val_idx[val].pop()

            # 删除val
            self.arr[pos] = last
            self.arr.pop()

            # 更新 last 的位置
            self.val_idx[last].remove(last_pos)
            self.val_idx[last].add(pos)



            return True




    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()