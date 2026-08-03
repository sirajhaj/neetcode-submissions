class MyHashSet:

    def __init__(self) :
        self.capacity = 101
        self.arr = [-1]*self.capacity
        self.size = 0

    def _resize(self) ->None:
        old_arr = self.arr
        self.capacity *= 2
        self.capacity += 3
        self.arr = [-1]*self.capacity
        self.size = 0

        for item in old_arr :
            if item != -1 :
                self.add(item)



    def add(self, key: int) -> None:
        if self.contains(key) == True :
            return
        if (self.size/self.capacity) >= 0.7 :
            self._resize()
        index = key % self.capacity
        while index<self.capacity and self.arr[index] != -1 :
            index+=1
        if index < self.capacity :
            self.arr[index] = key
            self.size +=1

    def remove(self, key: int) -> None:
        index = key % self.capacity
        while index < self.capacity and self.arr[index] !=key :
            index +=1
        if index < self.capacity :
            self.arr[index] = -1
            self.size -= 1

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