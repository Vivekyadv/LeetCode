import array
class MyHashMap:

    def __init__(self):
        self.store = array.array('i', [-1]) * 10

    def put(self, key: int, value: int) -> None:
        self.store[key] = value

    def get(self, key: int) -> int:
        return self.store[key]

    def remove(self, key: int) -> None:
        self.store[key] = -1
    
    def __str__(self) -> str:
        print(self.store)
        return ''


obj = MyHashMap()
obj.put(3,1018)
print(obj.get(5))
obj.remove(2)
print(obj)