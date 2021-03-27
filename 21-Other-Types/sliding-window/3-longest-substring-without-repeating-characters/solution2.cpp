// 滑动窗口法
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 统计字符出现的次数
        int freq[256] = {0};
        int l = 0, r = -1;
        int res = 0;

        while (l < s.size()) {
            // 右边界上的元素没有出现的时候
            if (r + 1 < s.size() && freq[s[r + 1]] == 0) {
                // r++;
                // freq[s[r]]++;
                freq[s[++r]]++;
            }
            else               
                // freq[s[l]]--;
                // l++;
                freq[s[l++]]--;

            res = max(res, r - l + 1);
        }

        return res;
    }
};