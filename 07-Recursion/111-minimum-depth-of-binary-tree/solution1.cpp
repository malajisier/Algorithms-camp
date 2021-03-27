/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// c++版本的递归
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        int ldepth = minDepth(root->left);
        int rdepth = minDepth(root->right);
        // 左孩子或右孩子为空时，其中之一为0，所以两者可相加
        // 都不为空时，返回较小者
        return root->left == nullptr || root->right == nullptr ? ldepth + rdepth + 1 : min(ldepth, rdepth) + 1;
    }
};