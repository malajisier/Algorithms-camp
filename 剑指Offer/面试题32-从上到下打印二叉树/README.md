## 32-二叉树打印系列
- i：二叉树的按层打印
- ii：额外要求，每一层打印一行
- iii：“之”形打印，变化每层的打印顺序    



## 32-i  从上到下打印二叉树      

### 题目描述：   
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印        


### 解题思路：   
- 二叉树的层次遍历
- 队列的使用


#### （1）python解法一：BFS
```Python 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TC:O(N),N 为二叉树的节点数量
# SC:O(N), 最差情况下，即当树为平衡二叉树时，最多有N/2个树节点同时在 queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, dq = [], collections.deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            res.append(node.val)
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        return res

```   

#### （2）python解法二：DFS
```Python


```



## 32-ii  从上到下 分层打印二叉树    



## 32-iii  从上到下 分层变序打印二叉树    


（1）python解法一
```Python
# 奇数层：值 从头到尾 输出
# 偶数层：值 从尾到头 输出
# 奇偶层判定：根据res 里的list个数，

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])

        while deque:
            level = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()

                # 余数是否为1，如果为1 则res中的层数是偶数个，现在这一层是奇数层
                if len(res) % 2:
                    # 偶数层，元素依次添加至头部
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(level))
        
        return res
```