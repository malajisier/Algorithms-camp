- TC: O(S.length+T.length)，遍历S、T花费的时间
- SC: O(T.length), 统计 26 个小写字母的空间，和存储最终排好序的字符串 T 的空间
```java
class Solution {
    public String customSortString(String S, String T) {
        StringBuilder sb = new StringBuilder();

        // 记录 T每个字符出现次数
        int[] rec = new int[26];
        for (char c : T.toCharArray()) {
            rec[c - 'a']++;
        }

        // 遍历S 中也存在于T 的字符，把该字符全部加入
        for (char c : S.toCharArray()) {
            if (rec[c - 'a'] != 0) {
                // 字符可能不止一个
                for (int i = 0; i < rec[c - 'a']; i++) {
                    sb.append(c);
                }
                // 添加结束后置为0
                rec[c - 'a'] = 0;
            }
        }

        // 把T 剩余的字符 添加进去
        for (int i = 0; i < rec.length; i++) {
            if (rec[i] != 0) {
                for (int j = 0; j < rec[i]; j++) {
                    sb.append((char)(i + 'a'));
                }
            }
        }
        return sb.toString();
    }
}
```

