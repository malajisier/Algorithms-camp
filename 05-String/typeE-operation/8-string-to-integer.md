```java
// 去掉空格，开头必须是符号或数字，超范围则截断
class Solution {
    public int myAtoi(String s) {
        int n = s.length();
        if (n == 0 || s.equals("")) return 0;

        int idx = 0, sign = 1, res = 0;
        // 去掉空格，不能使用trim(),会生成新的字符串
        while (idx < n-1 && s.charAt(idx) == ' ') {
            idx++;
        }
        if (idx == n) return 0;

        if (s.charAt(idx) == '+' || s.charAt(idx) == '-') {
            // // 简写
            // sign = s.charAt(idx) == '+' ? 1 : -1;
            // idx++;

             if (s.charAt(idx) == '+') {
                sign = 1;
                idx++;
            } else if (s.charAt(idx) == '-') {
                sign = -1;
                idx++;
            } else {
                return 0;
            }
        }

        while (idx < n) {
            int num = s.charAt(idx) - '0';
            if (num < 0 || num > 9) break;

            // res*10 和 res+num 都有可能越界
            if (Integer.MAX_VALUE/10 < res || 
                Integer.MAX_VALUE/10 == res && Integer.MAX_VALUE%10 < num) {
                    return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            res = res * 10 + num;
            idx++;
        }
        return sign * res;
    }
}
```