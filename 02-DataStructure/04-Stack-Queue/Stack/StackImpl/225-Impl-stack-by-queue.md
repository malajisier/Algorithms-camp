### 法一：双队列实现    

```java
class MyStack {
    Queue<Integer> input;
    Queue<Integer> data;

    public MyStack() {
        input = new LinkedList<>();
        data = new LinkedList<>();
    }
    
    public void push(int x) {
        input.offer(x);
        while (!data.isEmpty()) {
            input.offer(data.poll());
        }
        Queue tmp = input;
        input = data;
        data = tmp;
    }
    
    public int pop() {
        return data.poll();     
    }
    
    public int top() {
        return data.peek();
    }
    
    public boolean empty() {
        return data.isEmpty();
    }
}
```   
        

### 法二：单队列实现   

```java
