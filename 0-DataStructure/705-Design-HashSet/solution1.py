# 数组+链表，使用node模拟链表

class MyHashSet:
    def __init__(self):
        self.keyRange = 671
        self.bucket = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucket[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucket[bucketIndex].delete(key)
    
    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucket[bucketIndex].exists(key)


class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode


class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def exists(self, value):
        cur = self.head.next
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
    
    def delete(self, value):
        pre = self.head
        cur = self.head.next
        while cur is not None:
            if cur.value == value:
                pre.next = cur.next
                return False
            pre = cur
            cur = cur.next
