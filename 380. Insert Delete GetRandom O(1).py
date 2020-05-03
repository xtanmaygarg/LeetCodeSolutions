class RandomizedSet:

    def __init__(self):
        self.Set = []
        self.Map = dict()

    def insert(self, val: int) -> bool:
        if val not in self.Map:
            self.Set.append(val)
            self.Map[val] = len(self.Set) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.Map:
            self.Map[self.Set[-1]] = self.Map[val]
            self.Set[self.Map[val]] = self.Set[-1]
            del self.Map[val]
            self.Set.pop()
            return True
        return False

    def getRandom(self) -> int:
        from random import randint
        return self.Set[randint(0, len(self.Set) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
