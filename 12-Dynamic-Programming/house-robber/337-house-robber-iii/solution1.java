// 方法一：暴力递归 + 最优子结构
// 最优子结构： 爷爷节点+四个孙子节点 VS 两个儿子节点偷得钱
class Solution {
    public int rob(TreeNode root) {
        if (root == null) return 0;

        int money = root.val;
        // 爷爷节点+四个孙子节点
        if (root.left != null) {
            money += (rob(root.left.left) + rob(root.left.right));
        }
        if (root.right != null) {
            money += (rob(root.right.left) + rob(root.right.right));
        }

        return Math.max(money, rob(root.left) + rob(root.right));
    }
}

// 方法二：记忆化+优化重复子问题 
// 优化重复子问题：计算4个孙子节点时，也计算了两个儿子节点，在儿子当爷爷节点时，就会产生重复计算     
class Solution {
    public int rob(TreeNode root) {
        HashMap<TreeNode, Integer> memo = new HashMap<>();
        return myrob(root, memo);
    }

    public int myrob(TreeNode root, HashMap<TreeNode, Integer> memo) {
        if (root == null) return 0;

        if (memo.containsKey(root)) return memo.get(root);

        int money = root.val;
        if (root.left != null) {
            money += (myrob(root.left.left, memo) + myrob(root.left.right, memo));
        }        
        if (root.right != null) {
            money += (myrob(root.right.left, memo) + myrob(root.right.right, memo));
        }

        int res = Math.max(money, myrob(root.left, memo) + myrob(root.right, memo));
        memo.put(root, res);
        
        return res;
    }
}


// 方法三：递归 + 树型动态规划
// 使用数组定义，每个节点偷或不偷的两种状态，0是不偷，1是偷
// 状态：（1）当前节点偷，两个孩子节点不能偷了，（2）当前节点不偷，两个孩子只需要拿最多的钱出来
// 对于任一节点，能偷到的最大钱的状态:
// （1）当前节点不偷：最大钱数 = 左孩偷的钱 + 右孩偷的钱
// （2）当前节点偷：最大钱数 = 左孩不偷时的最大钱数 + 右孩不偷时的最大钱数 + 当前节点的钱数
class Solution {
    public int rob(TreeNode root) {
        int[] res = myrob(root);
        return Math.max(res[0], res[1]);
    }

    public int[] myrob(TreeNode root) {
        int[] res = new int[2];
        if (root == null) return res;

        int[] left = myrob(root.left);
        int[] right = myrob(root.right);

        res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        res[1] = left[0] + right[0] + root.val;

        return res;
    }
}