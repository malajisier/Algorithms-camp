两个队列的实现  
```python
class MyStack:
    def __init__(self):
        # q1 存储栈内的元素，q2辅助入栈操作
        self.queue1 = collections.deque()
        self.queue2 = collections.deque() 

    def push(self, x: int) -> None:
        # 新入栈元素在q2队首
        self.queue2.append(x)

        # 把 q1存储的栈内元素，依次加到q2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
            
        # q2 就能保证新入队的队首元素 是栈顶元素，直接赋给q1存储
        # q2再次置空
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not bool(self.queue1)
```

```java
class MyStack {
    // q1 存储栈内的元素，q2辅助入栈操作
    Queue<Integer> q1;
    Queue<Integer> q2;

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }
    
    public void push(int x) {
        q2.offer(x);
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }
        Queue<Integer> tmp = q1;
        q1 = q2;
        q2 = tmp;   
    }
    
    public int pop() {
        return q1.poll();
    }
    
    public int top() {
        return q1.peek();
    }
    
    public boolean empty() {
        return q1.isEmpty();
    }
}
```

