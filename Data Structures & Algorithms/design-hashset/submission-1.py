class MyHashSet:

    def __init__(self) :
        self.capacity = 101
        self.arr = [-1]*self.capacity

    def _resize(self,key) ->None:
        old_arr = self.arr
        self.capacity *= 2
        self.capacity += 1
        self.arr = [-1]*self.capacity

        for item in old_arr :
            if item != -1 :
                self.add(item)
        self.add(key)



    def add(self, key: int) -> None:
        if self.contains(key) == True :
            return
        index = key % self.capacity
        while index<self.capacity and self.arr[index] != -1 :
            index+=1
        if index == self.capacity :
            self._resize(key)
        else :
            self.arr[index] = key

    def remove(self, key: int) -> None:
        index = key % self.capacity
        while index < self.capacity and self.arr[index] !=key :
            index +=1
        if index < self.capacity :
            self.arr[index] = -1

    def contains(self, key: int) -> bool:
        index = key % self.capacity
        while index < self.capacity and self.arr[index] != key:
            index+=1
        if index < self.capacity :
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)