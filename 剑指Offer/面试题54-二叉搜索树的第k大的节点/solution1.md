https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/comments/379848   

根据二叉搜索树 中序遍历是有序的特性     

```Java
/** 法一：
 * 把中序遍历后的结果存到数组，取第k大 
 * 但 时间复杂度为O(n)，可以优化成 取到第k大 提前返回
 */
class Solution {
    public int kthLargest(TreeNode root, int k) {
        List<Integer> list = new ArrayList<>();
        helper(root, list);
        return list.get(list.size() - k);
    }

    private void helper(TreeNode root, List<Integer> list) {
        if (root == null) return;

        if (root.left != null) {
            helper(root.left, list);
        }
        list.add(root.val);
        if (root.right != null) {
            helper(root.right, list);
        }
    }
}

// 法二：
class Solution {
    // 注意：这里res，cnt 要取全局变量
    private int res = 0, cnt = 0;

    public int kthLargest(TreeNode root, int k) {
        if (root != null) {
            // 使用倒序的中序遍历，取第k大
            kthLargest(root.right, k);
            if (++cnt == k) {
                return (res = root.val);
            }
            kthLargest(root.left, k);
        }
        return res;
    }
}


```