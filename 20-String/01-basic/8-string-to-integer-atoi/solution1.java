class Solution {
    public int myAtoi(String str) {
        char[] s = str.toCharArray();
        int n = s.length, idx = 0, flag = 1, res = 0;

        // 去除字符串中的空格
        while (idx < n && s[idx] == ' ') {
            idx++;
        } 
        
        // 处理极端情况：多个空格的字符串， "      "
        if (idx == n) {
            return 0;
        }

        if (s[idx] == '+' || s[idx] == '-') {
            flag = s[idx] == '+' ? 1 : -1;
            idx++;
        }

        while (idx < n && Character.isDigit(s[idx])) {
            int digit = s[idx] - '0';
            // res*10 和 + digit 都有可能越界
            if (res > (Integer.MAX_VALUE - digit) / 10) {
                return flag == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            res = res * 10 + digit;
            idx++;
        }
        return flag * res;
    }
}