# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-ii-dui-lie-de-zui-da-zhi-by-leetcod/

# 三个函数的均摊时间复杂度，要求为O(1)
# pop_front,pop_back两个函数，直接使用队列就可以实现 O(1)的复杂度

# max_value函数，面临的一个问题：最大值出队后，无法知道下一个的最大值
# 思路：使用双端队列，记录最大值出队后，队列下一个最大值
# 时间复杂度：
# 虽然插入操作时最多可能会有 n 次出队操作，但每个数字只会出队一次，均摊到每个插入操作，就是O(1)


import queue
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        # 如果队尾元素 小于入队元素，则将小于value 的元素全部出队，再将value入队
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)


    def pop_front(self) -> int:
        if not self.deque:
            return -1
        res = self.queue.get()
        if res == self.deque[0]:
            self.deque.popleft()
        return res