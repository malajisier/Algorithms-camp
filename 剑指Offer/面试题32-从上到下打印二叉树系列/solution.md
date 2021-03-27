[toc]

## 32-二叉树打印系列

- i：二叉树的按层打印
- ii：额外要求，每一层打印一行
- iii：“之”形打印，变化每层的打印顺序    



### 32-i  从上到下打印二叉树      

题目描述：   

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印        

解题思路：   

- 二叉树的层次遍历
- 队列的使用


#### 法一：BFS
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

#### 法二：DFS
```Python


```



### 32-ii  从上到下 分层打印二叉树    

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, dq = collections.deque(), collections.deque()
        dq.append(root)

        while dq:
            tmp = []
            for i in range(len(dq)):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.appendleft(tmp)

        return res
```





### 32-iii  从上到下 分层变序打印二叉树，“之”字形打印    

#### 法一：BFS

两个方法确定奇偶层

- 设置标志，每层转一次

- 根据根据res 里的list个数

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {      
        List<List<Integer>> res = new LinkedList<>();
        if (root == null) return res;

        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.offer(root);
        // 偶数层 设为true
        boolean leftBegin = true; 

        while (!nodes.isEmpty()) {
            Deque<Integer> perLevel = new LinkedList<>();
            int size = nodes.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = nodes.poll();
                if (leftBegin) {
                    perLevel.offerLast(node.val);
                } else {
                    perLevel.offerFirst(node.val);
                }
                if (node.left != null) nodes.offer(node.left);
                if (node.right != null) nodes.offer(node.right);
            }
            res.add(new LinkedList<Integer>(perLevel));
            leftBegin = !leftBegin;
        }
        return res;
    }
}
```



```Python
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



#### 法二：DFS，递归

```python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, level):
            if not root: return
            if len(res) == level: # 刚进入这一层，初始化[]
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
     
        helper(root, 0)
        return res
```

