### 双指针，贪心

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int p1 = 0;
        int p2 = 0;
        int sLen = s.length();
        int tLen = t.length();

        while (p1 != sLen && p2 != tLen) {
            if (s.charAt(p1) == t.charAt(p2)) {
                p1++;
                p2++;
            } else {
                p2++;
            }
        }

        return p1 == sLen;
    }
}

```