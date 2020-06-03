// TC:O(S)，S为所有字符串长度总和   SC:O(1)

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        // 遍历每一列
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs.charAt(i);

            // 遍历每个字符串
            for (int j = 0; j < strs.length(); j++) {

                // 比较每个字符时，如果相等，继续循环下去
                // 不相等时，说明已经找到了相同的前缀
                if (i == strs[j].length() || strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }

        return strs[0];
    }
}