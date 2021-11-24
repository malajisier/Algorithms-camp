```java
/**
 * Stack 是Vector的子类
 包含方法：Stack(), empty(), pop(),push(), peek()
 */
class MinStack {
    Stack<Integer> stack1;
    Stack<Integer> stack2;

    /** initialize your data structure here. */
    public MinStack() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.add(x);
        if (stack2.isEmpty() || x <= stack2.peek()) {
            stack2.add(x);
        }
    }
    
    public void pop() {
        if (stack1.pop().equals(stack2.peek())) {
            stack2.pop();
        }
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int min() {
        return stack2.peek();
    }
}
```


```python
class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x) 

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
```