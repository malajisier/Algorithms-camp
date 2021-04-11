// 剪枝优化的回溯算法   
// https://leetcode-cn.com/problems/combinations/solution/dfsjian-zhi-by-rouzi/

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, n, k, 0, -1);
        return res;
    }

    // pre: 记录前一次递归时的取值，在pre之后进行本次的取值的选择，这样避免数值以及组合的重复
    // pos: 表示当前操作位置，即当前进行的是K个数中的第pos个的取值操作
    // 利用pre值以及当前位置pos与K的关系进行剪枝

    void dfs(vector<vector<int>>& res, vector<int>& tmp, int n, int k, int pos, int pre) {
        if (pos == k) {
            res.push_back(tmp);
            return;
        }
        
        //剪枝，添加之后用时节省了2/3
        //在当前对不合理的取值进行判断，结束下一层的递归操作。
        //如果当前剩余可操作数字的个数即（n-pre）< k-pos+1(即组合中有待赋值的位置个数)
        // （+1是因为当前pos还没有进行操作），则可以判断该条路径不可能得到正确的解，不再向下探寻。

        if ((pos + (n - pre)) <= k) return;

        for (int i = pre + 1; i < n; i ++) {
            tmp.push_back(i + 1);
            pre = i;
            dfs(res, tmp, n, k, pos + 1, pre);
            tmp.pop_back();
        }

        return;
    }
};


// // 打印信息来理清执行过程    
// void dfs(vector<vector<int>>& res, vector<int>& tmp, int n, int k, int pos, int pre) {
//         cout << "pos = " << pos << endl;
//         cout << "--------" << endl;

//         if (pos == k) {
//             res.push_back(tmp);
    
//             return;
//         }
        
//         if ((pos + (n - pre)) <= k) return;

//         for (int i = pre + 1; i < n; i ++) {
//             tmp.push_back(i + 1);

//             for (int i = 0; i < tmp.size(); i ++)
//                 cout << "tmp:" << tmp[i] << endl;
//             cout << "**********" << endl;

//             pre = i;
//             cout << "pre: " << pre << endl;
//             cout << "^^^^^^^" << endl;

//             dfs(res, tmp, n, k, pos + 1, pre);

//             tmp.pop_back();
//             for (int i = 0; i < tmp.size(); i ++)
//                 cout << "tmp: " << tmp[i] << endl;
//             cout << "&&&&&&&&&" << endl;
//         }

//         return;
//     }