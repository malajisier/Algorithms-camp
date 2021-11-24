- TC:O(1), 每个元素至多入栈出栈一次，n个元素平均下来为O(1)
- SC:O(n)

```java
// 常用方法： addLast(), removeLast()
//栈只能操作栈顶元素

class CQueue {
    LinkedList<Integer> stack_in, stack_out;

    public CQueue() {
        stack_in = new LinkedList<>();
        stack_out = new LinkedList<>();
    }
    
    public void appendTail(int value) {
        stack_in.addLast(value);
    }
    
    public int deleteHead() {
        if (stack_out.isEmpty()) {
            if (!stack_in.isEmpty()) {
                while (!stack_in.isEmpty()) {
                    stack_out.addLast(stack_in.removeLast());
                }
                return stack_out.removeLast();
            } else {
                return -1;
            }
        }
        return stack_out.removeLast();
    }
```


```python
class CQueue:
    def __init__(self):
        self.s_in = []
        self.s_out = []

    def appendTail(self, value: int) -> None:
        self.s_in.append(value)

    def deleteHead(self) -> int:
        if not self.s_out:
            if self.s_in:
                while self.s_in:
                    self.s_out.append(self.s_in.pop())
            else:
                return -1
        
        return self.s_out.pop()
```