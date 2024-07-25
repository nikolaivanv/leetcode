import random


class RandomizedSet:

    def __init__(self):
        self.last_index = -1
        self.dict = dict()
        self.list = []

    def insert(self, val: int) -> bool:
        if not val in self.dict:
            if self.last_index < len(self.list) - 1:
                self.list[self.last_index+1] = val
            else:
                self.list.append(val)
            self.last_index = self.last_index + 1
            self.dict[val] = self.last_index
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            i = self.dict[val]
            del self.dict[val]
            if i < self.last_index:
                v = self.list[self.last_index]
                self.dict[v] = i
                self.list[i] = v
            self.last_index = self.last_index - 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        i = random.randrange(0, self.last_index+1)
        return self.list[i]