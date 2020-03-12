// 利用unordered_map的实现，结尾返回值有问题，报错
// 
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string t) {
        // 记录最短子串的开始位置和最小长度
        int start = 0, min_len = INT_MAX;
        int l = 0, r = 0;

        // 两个哈希表作为计算器
        // needs记录给定的t，包含的字符和出现次数， window记录当前窗口包含的字符和出现次数
        unordered_map<char, int> window;
        unordered_map<char, int> needs;

        for (char c : t) needs[c]++;
        // match记录window中符合要求的字符数量
        int match = 0;

        while (r < s.size()) {
            char s1 = s[r];
            // 若给定的t 包含字符s1
             if (needs.count(s1)) {
                 window[s1]++;
                 // 字符s1的出现次数符合要求了
                 if (window[s1] == needs[s1])
                    match++;
             }
             r++;
        

            // 窗口包含的字符，已经符合needs的要求了
            while (match == needs.size()) {
                if (r - l < min_len) {
                    // 更新最小子串的位置和长度
                    start = l;
                    min_len = r- l;
                }

                char s2 = s[l];
                if (needs.count(s2)) {
                    window[s2]--;
                    // 字符 s2 出现次数不再符合要求
                    if (window[s2] < needs[s2])
                        match--;
                }
                l++;
            }
        }
        return min_len == INT_MAX ?
                "" : s.substr(start, min_len);
    }
};
    
