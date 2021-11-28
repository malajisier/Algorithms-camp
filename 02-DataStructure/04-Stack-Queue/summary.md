### 1. Stack   
先入后出；添加、删除均为O(1)，查询为O(n)   



Java提供的栈
- Queue 和Deque都是继承于Collection，Deque是Queue的子接口
- Queue有一个直接子类PriorityQueue，而Deque中直接子类有两个：ArrayDeque, LinkedList。LinkedList 又是List的子类     


PriorityQueue方法：  
- 插入：
  - add(E e)：插入失败 抛出异常
  - offer(E e)：插入失败返回false
- 删除队首：
  - remove(): 失败抛出异常
  - poll(): 失败返回null
- remove(Object o):
  删除与 o相等的元素，即使有多个相等，也只删一个
- 获取队首元素：
  - element(): 失败 抛出异常
  - peek(): 失败返回null
- 






References:
https://blog.csdn.net/weixin_42091177/article/details/112734703    





- java 字符、整数转化
  - int to String:
    ```java
    Integer.toString(i)
    String.valueOf(i)
    ```
    
  - String to int:
  
    ```
    Integer.parseInt(s)
    Integer.valueOf(s).intValue()
    ```
  
  - 判断字符是否为数字
  
    ```
    Character.isDigit(str.charAt(i))
    ```
  













### 2. Queue   
先入先出；添加、删除均为O(1)，查询为O(n)

- 顺序队列：数组实现的
- 链式队列：链表实现



#### 队列常用方法比较：   
- poll: 弹出队列的首个元素，如果队列为空，返回null
- peek: 查看队列的首个元素，如果队列为空，返回null
- element：查看队列的首个元素，如果队列为空，抛出异常NoSuchElementException



```java
// 数组实现
public class ArrayQueue {
    private String[] items;
    private int n = 0;
    private int head = 0;
    private int tail = 0;
    
    
    public ArrayQueue(int capacity) {
        items = new String[capacity];
        n = capacity;
    }
    
    public boolean enqueue(String item) {
        if (tail == n) return false;
        items[tail++] = item;
        return true;
    }
    
    public String dequeue() {
        if (head == tail) return false;
        String ret = items[head++];
        return ret;
    }
}


// 优化一：数据搬迁
// 频繁删除导致数组的不连续，但当每次出队都进行搬迁，时间复杂度会变为O(n)
// 只需要在没有空闲空间时，触发一次数据搬迁即可
public boolean enqueue(String item) {
    if (tail == n) {
        // 整个队列都已占满
        if (head == 0) return false;
        for (int i = head; i < tail; i++) {
            items[i - head] = items[i];
        }
        tail -= head;
        head = 0;
    }
    
    items[tail++] = item;
    return true;
}
```









#### 2.1 Deque: Double-End Queue   

双端队列，栈和队列的结合体，在头尾均可执行push、pop操作    
(1) Python    
- heapq
- 高性能的'container'库
