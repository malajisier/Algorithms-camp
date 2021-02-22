### 1. Stack   
先入后出；添加、删除均为O(1)，查询为O(n)   



- Java提供的栈
  - Queue以及Deque都是继承于Collection，Deque是Queue的子接口
  - Queue有一个直接子类PriorityQueue，而Deque中直接子类有两个：ArrayDeque, LinkedList。LinkedList 又是List的子类

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



#### 队列常用方法比较：   
- poll: 弹出队列的首个元素，如果队列为空，返回null
- peek: 查看队列的首个元素，如果队列为空，返回null
- element：查看队列的首个元素，如果队列为空，抛出异常NoSuchElementException





#### 2.1 Deque: Double-End Queue   

双端队列，栈和队列的结合体，在头尾均可执行push、pop操作    
(1) Python    
- heapq
- 高性能的'container'库
