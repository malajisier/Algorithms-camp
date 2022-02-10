### 法一：滑动窗口 + 模拟字典
参考：https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-by-leetcode-q6tp/

```java
// 评论中的精华版代码
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] freq = new int[26];
        int cnt = 0;
        int n1 = s1.length(), n2 = s2.length();

        for (char c : s1.toCharArray()) {
            // cnt 统计s1的字符种类
            if (freq[c - 'a'] == 0) {
                cnt++;
            }
            freq[c - 'a']++;
        }

        char[] ch2 = s2.toCharArray();
        for (int i = 0; i < n2; i++) {
            // 相当于左边界
            // 滑动窗口里 字符的 累计出现次数 满足s1 字符的次数，种类-1
            if (--freq[ch2[i] - 'a'] == 0) {
                cnt--;
            }

            // 相当于右边界
            // 滑动窗口到右边界
            if (i >= n1 && freq[ch2[i - n1] - 'a']++ == 0) {
                cnt++;
            }
            if (cnt == 0) {
                return true;
            }
        }
        return false;
    }
}
```