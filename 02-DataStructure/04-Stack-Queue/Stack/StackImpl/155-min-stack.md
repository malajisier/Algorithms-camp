### 法一：辅助栈   
```java
class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int x) {
        stack.push(x);
        if (!minStack.isEmpty()) {
            if (x <= minStack.peek()) {
                minStack.push(x);
            }
        } else {
            minStack.push(x);
        }
    }

    public void pop() {
        int pop = stack.pop();
        if (pop == minStack.peek()) {
            minStack.pop();
        }

    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}








```



### 法二：不借助额外空间    
- 思路：保存差值      
- 时间：O(n), 空间:O(1)     

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = -1

    def push(self, val: int) -> None:
        # 初始化栈
        if not self.stack:
            self.stack.append(0)
            self.min_val = x
        else:
            diff = x - self.min_val
            self.stack.append(diff)  # 栈 保存差值，配合min_val 可得出真实值
            self.min_val = self.min_val if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            # diff
            if diff < 0:
                top = self.min_val
                self.min_val = top - diff
            else:
                top = self.min_val + diff
            return top

    def top(self) -> int:
        return self.min_val if self.stack[-1] < 0 else self.min_val + self.stack[-1]

    def getMin(self) -> int:
        return self.min_val if self.stack else -1
```