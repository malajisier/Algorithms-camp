使用api，不推荐

```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        strs = s.split()
        strs.reverse()
        return ''.join(strs)
```


```Java
class Solution {
    public String reverseWords(String s) {
        String[] strs = s.trim().split();
        StringBuilder res = new StringBuilder();

        for (int i = s.length() - 1; i >=0; i--) {
            if (strs[i].equals("")) continue;
            res.append(strs[i] + " ");
        }

        return res.toString().trim();
    }
}
```