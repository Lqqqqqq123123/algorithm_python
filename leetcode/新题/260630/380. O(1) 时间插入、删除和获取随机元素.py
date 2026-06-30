class RandomizedSet:

    def __init__(self):
        self.arr = [] # 为了后续随机获取元素
        self.val_idx = {} # 记录值 -> list 中索引


    @property
    def n(self):
        return len(self.arr)

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        # 插入
        self.arr.append(val)
        self.val_idx[val] = self.n - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False

        # 删除
        # 1. 先获取索引
        idx = self.val_idx[val]
        # 2. 删除(为了O（1），要把删除的元素放到末尾，然后删除末尾元素)
        self.val_idx[self.arr[-1]] = idx
        self.val_idx.pop(val)

        self.arr[idx] = self.arr[-1]
        self.arr.pop()




    def getRandom(self) -> int:
        return self.arr[random.randint(0, self.n - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()