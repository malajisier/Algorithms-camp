class Solution {
public:
    map<int, int> pos;
    vector<int> preorder, inorder;

    TreeNode* buildTree(vector<int>& _preorder, vector<int>& _inorder) {
        preorder = _preorder, inorder = _inorder;
        for (int i = 0; i < inorder.size(); i ++) pos[inorder[i]] = i;
        return recBuild(0, preorder.size() - 1, 0, inorder.size() - 1);   
    }

    TreeNode * recBuild(int pl, int pr, int il, int ir) {
        if (pl > pr) return nullptr;

        auto root = new TreeNode(preorder[pl]);
        int pivot = pos[root->val];
        root->left = recBuild(pl + 1, pl + pivot - il, il, pivot);
        root->right = recBuild(pl + pivot - il + 1, pr, pivot + 1, ir);
        return root;
    }

};


