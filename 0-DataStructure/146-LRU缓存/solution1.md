## 设计并实现LRU      
https://leetcode-cn.com/problems/lru-cache-lcci/solution/linkedhashmap-shuang-lian-biao-hashmap-dan-lian-2/ 


要求：  
实现get、put操作

思路：   
（1）使用双向链表存储键值对，靠近头部的键值对是最近使用的，靠近尾部的是最久未使用的    
（2）使用哈希表，存储 数据的键在链表中的位置    

具体方法：
（1）





```Python
# 定义节点
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key存在，通过哈希表定位，再将节点移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key不存在，创建一个新节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果添加节点后 容量超出，则删除尾部节点
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key存在，先通过哈希表定位，再修改value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
