/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// 思路和py版本的类似，都使用了全局变量、额外dict、递归分治的方法

#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    map<int, int> pos;
    vector<int> preorder, inorder;

    TreeNode* buildTree(vector<int>& _preorder, vector<int>& _inorder) {
        preorder = _preorder, inorder = _inorder
        for (int i = 0; i < inorder.size(); i ++) pos[inorder[i]] = i;
        return recBuild(0, preorder.size() - 1, 0, inorder.size() - 1);
    }

    TreeNode* recBuild(int prel, int prer, int inl, int inr) {
        if (prel > prer) return nullptr;
        auto root = new TreeNode(preorder[prel]);
        int k = pos[root->val];
        auto left = recBuild(prel + 1, prel + k - inl, inl, k - 1);
        auto right = recBuild(prel + (k - inl) + 1, prer, k + 1, inr);
        root->left = left, root->right = right;
        return root;
    }
};





