from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data_storage = OrderedDict()



    def get(self, key: int) -> int:
        if key in self.data_storage:
            self.data_storage.move_to_end(key)       # remove existing value to add it to the end - to show that iw was recently used
            return self.data_storage[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.data_storage[key] = value
        self.data_storage.move_to_end(key)  # remove existing value

        if self.capacity < len(self.data_storage):
            self.data_storage.popitem(last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)      # cache is {1=1}
lRUCache.put(2, 2)      # cache is {1=1, 2=2}
print(lRUCache.get(1))         # return 1
lRUCache.put(3, 3)      # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))         #     returns -1 (not found)
lRUCache.put(4, 4)      # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))         # return -1 (not found)
print(lRUCache.get(3))         # return 3
print(lRUCache.get(4))         # return 4