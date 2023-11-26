"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
    
 """

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # move the accessed element to the end
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # update the key and move it to the end
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove the least recently used element
    
    def get_all(self) -> None:
        return list(self.cache())
        
        
    def print_cache(self) -> None:
        print(self.cache)
        print( type(self.cache))

def test_LRUCache():
    # Test case 1
    lruCache = LRUCache(2)
    lruCache.put(1, 1)
    lruCache.put(2, 2)
    assert lruCache.get(1) == 1
    lruCache.put(3, 3)  # This will cause key 2 to be removed because the cache reached its capacity
    assert lruCache.get(2) == -1  # Key 2 was removed
    lruCache.put(4, 4)  # This will cause key 1 to be removed because it's the least recently used
    assert lruCache.get(1) == -1  # Key 1 was removed
    assert lruCache.get(3) == 3
    assert lruCache.get(4) == 4

    lruCache.print_cache()
    # Test case 2
    lruCache = LRUCache(1)
    lruCache.put(2, 1)
    assert lruCache.get(2) == 1
    lruCache.put(3, 2)  # This will cause key 2 to be removed because the cache reached its capacity
    assert lruCache.get(2) == -1  # Key 2 was removed
    assert lruCache.get(3) == 2
    
    lruCache.print_cache()
    

def sort_dict(user: dict)->dict :
    return {k: v for k, v in sorted(user.items(), key = lambda x: x[1])}
test_LRUCache()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)