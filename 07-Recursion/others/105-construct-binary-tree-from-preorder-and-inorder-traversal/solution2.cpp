class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return recBuild(preorder.begin(), preorder.end(), inorder.begin(), inorder.end());
    }

    TreeNode* recBuild(vector<int>::iterator preBegin, vector<int>::iterator preEnd, vector<int>::iterator inBegin, vector<int>::iterator inEnd) {
        if (inBegin == inEnd) return NULL;
        TreeNode* root = new TreeNode(*preBegin);
        // 在中序遍历里，找root的位置
        auto pivot = find(inBegin, inEnd, *preBegin);
        root->left = recBuild(preBegin + 1, pivot - inBegin + preBegin + 1, inBegin, pivot);
        root->right = recBuild(pivot - inBegin + preBegin + 1, preEnd, pivot + 1, inEnd);
        return root;
    }
};


