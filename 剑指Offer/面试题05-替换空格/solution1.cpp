class Solution {
public:
    string replaceSpace(string s) {
        string res;
        // C++11标准auto：变量的自动类型推断
        // 根据变量初始值的类型自动为此变量选择匹配的类型，类似的关键字还有decltype
        for (auto c : s) {
            if (c == ' ') {
                res += "%20";
            }
            else
                res += c;
        }

        return res;
    }
};