## 重点：
（1）二叉树的层次遍历，递归方法、迭代方法（使用队列）---102.在BFS中


### 1. 树
树和图 最关键的一个差别：有没有环       

（1）树中结点的示例代码：   
```Python
# Python
class TreeNode:
    def __init__(self, init):
        self.val = val
        self.left, self.right = None, None

```    

```C++
// C++
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
}
```   

（2）遍历方式   
- 前序遍历 
```Python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

```     

- 中序遍历
```Python
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)
```

- 后序遍历
```Python
def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```
- 层次遍历


### 2. 二叉搜索树          
又名有序二叉树、排序二叉树，是指一棵空树或具有下列性质的二叉树：   
- 左子树上所有结点的值，均小于它的根节点的值
- 右子树上所有结点的值，均大于它的根节点的值
- 以此类推，左右子树也分别为二叉搜索树           

由性质可以得出，二叉搜索树的中序遍历是升序的       
  
（1）常见操作    
查询、创建（插入新节点）、删除， 时间复杂度均为 log(n)，对比普通二叉树的 O(n)，相当于加速了        
 

二叉树常用的操作   
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-he-di-gui-by-powcai/