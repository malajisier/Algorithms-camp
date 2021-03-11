/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
class Solution {
    Map<TreeNode, Integer> memo = new HashMap<>();

    public int rob(TreeNode root) {
        if (root == null) return 0;

        if (memo.containsKey(root)) 
            return memo.get(root);

        int doit = root.val 
                    + (root.left == null ? 0 : rob(root.left.left) + rob(root.left.right))
                    + (root.right == null ? 0 : rob(root.right.left) + rob(root.right.right));
        
        int notdo = rob(root.left) + rob(root.right);

        int res = Math.max(doit, notdo);
        memo.put(root, res);

        return res;
    }
}