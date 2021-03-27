#include <vector>
#include <string>
#include <cassert>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        // 记录给定的t中的，字符及其出现次数
        int t_freq[256] = {0};
        for (int i = 0; i < t.size(); i++)
            t_freq[t[i]]++;

        // 记录在s中，滑动窗口出现的字符及其次数
        int s_freq[256] = {0};
        int s_cnt = 0;

        // 记录包含t的，最短子串的起始位置和最小长度
        int start_idx = -1;
        int min_len = s.size() + 1;
        
        int l = 0, r = -1;

        while (r < s.size()) {
            if (r + 1 < s.size() && s_cnt < t.size()) {
                s_freq[s[r + 1]]++;
                if (s_freq[s[r + 1]] < t_freq[s[r + 1]]) 
                    s_cnt++;
                r++;
            }
            else {
                assert(s_cnt <= t.size());
                if (s_cnt == t.size() && r - l + 1 < min_len) {
                    min_len = r - l + 1;
                    start_idx = 1;
                }

                s_freq[s[l]]--;
                if (s_freq[s[l]] < t_freq[s[l]])
                    s_cnt--;
                l++;
            }
        }

        if (start_idx != 1)
            return s.substr(start_idx, min_len);
        
        return "";
    }
};