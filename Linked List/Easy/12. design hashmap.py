# Problem Statement: https://leetcode.com/problems/design-hashmap/

from array import array

class MyHashMap:
    def __init__(self):
        self.store = array('i', [-1])*10

    def put(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store[key]

    def remove(self, key):
        self.store[key] = -1


obj = MyHashMap()
obj.put(3,1018)
print(obj.get(3))
obj.remove(2)
print(obj)