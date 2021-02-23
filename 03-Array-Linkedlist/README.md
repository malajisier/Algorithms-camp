
### 链表的知识点
- 自定义ListNode
- 生成ListNode，从int、char数组转为 ListNode
- 输出链表的每个节点
- 熟悉LinkedList的常用方法
- 掌握常见List和数组之间的转换


### 链表题目
#### 类型一：链表加法
- 2-两数相加
- 面试题02.05-链表求和
- 445-两数相加ii


#### 类型二：反转链表  
- 206-反转链表
- 92-反转链表ii
- 剑指offer06-从尾到头打印链表
- 143-重排链表
- 25-k个一组反转链表
- 234-回文链表



### 重点代码 
 
1-定义链表
```java
class ListNode {
    int val;
    ListNode next;
    
    ListNode() {}
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}   
``` 

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        slef.next = None
```


2-生成链表
```java
public static ListNode create(int[] nums) {
    ListNode pre = new ListNode(0), cur = pre;
    for (int num : nums) {
        cur.next = new ListNode(num);
        cur = cur.next;
    }
    return pre.next;
}
```  

3-输出链表
```java
法一： 常规方法
public static void printList(ListNode head) {
    while (head != null) {
        if (head.next != null) {
            System.out.print(head.val + "->");
        } else {
            System.out.print(head.val);
        }
    }
    System.out.println();
}


法二：重写toString()
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }

    @override
    public String toString() {
        ListNode tmp = this;
        StringBuffer sb = new StringBuffer();
        while (tmp != null) {
            sb.append(tmp.val);
            if (tmp.next != null) {
                sb.append("->");
            }
            tmp = tmp.next;
        }
        return sb.toString();
    }
}
```


