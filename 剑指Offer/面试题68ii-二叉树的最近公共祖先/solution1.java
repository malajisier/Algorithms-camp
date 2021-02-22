/**
 * https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
 * https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/
 */

/**说明：
 * lowestCommonAncestor：这个函数理解为帮两个节点找祖先
 * 帮p和q找到一个祖先就行，找到两个就更好了，如果找不到就返回NULL 
 * 在root->left里面找一次，root->right里面再找一次
 * 
 * 结果：
 * 
 */



// 递归实现
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left != null && right != null) {
            return root;
        }

        // if (left != null ) {
        //     return left;
        // }

        // if (right != null) {
        //     return right;
        // }

        // return null;
        
        // 简化写法
        return left == null? right : left;
    }
}