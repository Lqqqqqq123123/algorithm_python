import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.val_index = {}


    @property
    def n(self):
        return len(self.arr)

    def insert(self, val: int) -> bool:
        if val not in self.val_index:
            self.arr.append(val)
            self.val_index[val] = self.n - 1

            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        idx = self.val_index[val]
        self.val_index[self.arr[-1]] = idx
        self.arr[idx] = self.arr[-1]
        self.arr.pop()
        del self.val_index[val]
        return True

    def getRandom(self) -> int:
        # 随机数生成
        return self.arr[random.randint(0, self.n - 1)]

# Your RandomizedSet object will be instanstiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()