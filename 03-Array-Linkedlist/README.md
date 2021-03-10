
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



#### 类型三：删除某个节点
- 剑指Offer18-删除链表的节点
- 237-删除链表中的节点
3. 19. 删除链表的倒数第N个节点
4. 83. 删除排序链表中的重复元素：给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
5. 82. 删除排序链表中的重复元素 II：给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。
6. 面试题 02.01. 移除重复节点：移除未排序链表中的重复节点。保留最开始出现的节点。
7. 203. 移除链表元素：删除链表中等于给定值val的所有节点


#### 类型四：其他操作-特性
- （1）排序
   - 142-链表的插入排序：要求时间复杂度O(n^2)
   - 148-排序链表：
     - 要求O(nlogn)的时间复杂度和常数级空间复杂度
     - O(nlogn)有快排、归并、堆排，但快排最差O(n^2)，最适合链表排序的是归并
     - 因为自顶向下是O(logn)，则O(1) 需要自底向上的方式
     - **快排版本：头条面试题**
- 









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


