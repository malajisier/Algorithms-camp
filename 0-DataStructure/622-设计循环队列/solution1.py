# 使用一维数组实现，通过操作索引来构建环
# TC:O(1),  SC:O(N): 固定空间，预分配的容量

# 参数：
# 队尾位置： tail = (head + size - 1) mod capacity
# capacity：不是必须的，可通过数组属性得到。但使用频率高，在python中需要调用len(queue)，java中调用queue.length更高效

# 官方题解：
# https://leetcode-cn.com/problems/design-circular-queue/solution/she-ji-xun-huan-dui-lie-by-leetcode/


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.headIdx = 0
        self.count = 0
        self.capacity = k


    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        # 在队尾索引的 下一个位置插入·
        self.queue[(self.headIdx + self.count) % self.capacity] = value
        self.count += 1
        return True


    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIdx = (self.headIdx + 1) % self.capacity
        self.count -= 1
        return True


    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIdx]


    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIdx + self.count - 1) % self.capacity]


    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity