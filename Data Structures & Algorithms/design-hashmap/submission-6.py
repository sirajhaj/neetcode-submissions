class TreeNode:
    def __init__(self, key: int,value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key: int,value: int):
        if not root:
            return TreeNode(key,value)
        if key < root.key:
            root.left = self.insert(root.left, key,value)
        elif key > root.key:
            root.right = self.insert(root.right, key,value)
        root.value = value
        return root

    def delete(self, root, key: int):
        if not root:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)
        return root

    def minValueNode(self, root):
        while root.left:
            root = root.left
        return root
    
    def search(self, root, key):
        if not root:
            return -1
        if key == root.key:
            return root.value
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def add(self, key: int, value: int):
        self.root = self.insert(self.root, key, value)

    def remove(self, key: int):
        self.root = self.delete(self.root, key)

class MyHashMap:

    def __init__(self): 
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        cur = self.buckets[key % len(self.buckets)]
        cur.add(key,value)
    def get(self, key: int) -> int:
        cur = self.buckets[key % len(self.buckets)]
        return cur.search(cur.root,key)
        

    def remove(self, key: int) -> None:
        cur = self.buckets[key % len(self.buckets)]
        cur.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)