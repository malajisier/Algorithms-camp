https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/marvelzhong-deng-de-xue-xi-bi-ji-889-by-tyanyone-2/

```java
class Solution {
    private int[] pre;
    private Map<Integer, Integer> idxMap;

    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        this.pre = pre;
        idxMap = new HashMap<>();
        for (int i = 0; i < post.length; i++) {
            idxMap.put(post[i], i);
        }
        return build(0, pre.length - 1, 0);    
    }

    private TreeNode build(int inL, int inR, int postL) {
            if (inL > inR) return null;
            TreeNode root = new TreeNode(pre[inL]);
            if (inL < inR) {
                int leftVal = pre[inL + 1]; // 默认有左子树，即左子树根节点位置
                int leftTreeSize = idxMap.get(leftVal) - postL + 1;  // postL:最左子节点位置
                root.left = build(inL + 1, inL + leftTreeSize, postL);
                root.right = build(inL + leftTreeSize + 1, inR, postL + leftTreeSize);
            }
            return root;
    } 
}
```