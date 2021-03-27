### 题目描述：       
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向     
  
### 解题思路：   
- 二叉搜索树的中序遍历是 **递增序列**
- pre、cur 两种指针构建双向链表的关系
- 头尾节点   

#### （1）python解法一：   
```Python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            
            # 递归左子树
            dfs(cur.left)
            # 双向链表
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                # 开始记录头节点
                self.head = cur
            # 指向下一个节点
            self.pre = cur

            dfs(cur.right)
        
        if not root: return
        # 初始化pre
        self.pre = None
        dfs(root)
        # 头尾节点互相指引
        self.head.left, self.pre.right = self.pre, self.head

        return self.root



```

#### 
```Java
class Solution {
    Node head, pre;
    public Node treeToDoublyList(Node root) {
        if (root == null) return null;
        dfs(root);
        head.left = pre;
        pre.right = head;

        return head;
    }

    void dfs(Node cur) {
        if (cur == null) return;
        dfs(cur.left);
        if (pre != null) {
            pre.right = cur;
            cur.left = pre;
        } else {
            head = cur;
        }
        pre = cur;
    }
}


```