class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        #initially wire them to each other
        self.left.next, self.right.prev=self.right, self.left
    def remove(self, node):
        #place holder
        prev, next = node.prev, node.next
        prev.next, next.prev =next, prev
    
    def insert(self, node):
        #place holder
        prev, next= self.right.prev, self.right
        prev.next=next.prev=node
        node.prev, node.next= prev, next
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            #since access, make it most recent, ie. remove and insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key]=newNode
        #check capacity
        if len(self.cache)>self.capacity:
            #remove lru
            node=self.left.next
            del self.cache[node.key]
            self.remove(node)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)