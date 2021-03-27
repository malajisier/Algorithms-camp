#### 法一：使用栈   
- 思路：
  - 核心技巧：
    - 栈里面每次存储两个信息, (左括号前的字符串, 左括号前的数字)
    - 比如abc3[def], 当遇到第一个左括号的时候，压栈("abc", 3), 然后遍历到def, 当遇到右括号的时候, 从栈里面弹出一个元素(s1, n1), 得到新的字符串为s1+n1*"def"
  - 遇到左括号就进行压栈处理，遇到右括号就弹出栈

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""  # 实时记录当前 可以提取出来的字符串

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)  # 遇到多位数字时方便计算
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0  # 压栈后重置，因为需要处理括号内的元素了
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        
        return res

```


#### 法二：递归  

```java
class Solution {
    // 记录 递归中for循环中 i的位置
    private static int numIdx = 0;
    public String decodeString(String s) {
        if (s.length() == 0) return "";
        char[] chars = s.toCharArray();
        return invoke(chars, 0);
    }

    public String invoke(char[] s, int idx) {
        // 每次递归中得到的 字符串
        StringBuilder sb = new StringBuilder();
        // 每次递归前 字符串的重复次数
        StringBuilder num = new StringBuilder();

        for (int i = idx; i < s.length; i++) {
            if ((s[i]>='a'&&s[i]<='z') || (s[i]>='A'&&s[i]<='Z')){
                sb.append(s[i]);
            } else if (s[i] >= '0' && s[i] <= '9') {
                num.append(s[i]);

            // 遇到左括号，进入递归
            } else if (s[i] == '[') {
                String inv  = invoke(s, i + 1);
                for (int j = 0; j < Integer.parseInt(num.toString()); j++) {
                    sb.append(inv);
                }
                // 清除之前保存的数字
                num.setLength(0);
                //设置i的值，因为递归，所以numIndex之前的字符都分析过了，下次循环就直接跳过就行
                i  = numIdx;
            } else if (s[i] == ']') {
                // 记录本次递归 i到达的位置
                numIdx = i;
                return sb.toString();
            }
    }
    return sb.toString();
    }
}

```