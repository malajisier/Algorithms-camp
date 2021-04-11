### 法一：双指针  
- 以左右括号、逗号，作为分界线
- 


```java
class Solution {
    public NestedInteger deserialize(String s) {
        if (s.chatAt(0) != '[') {
            return new NestedInteger(Integer.valueOf(s));
        }

        Deque<NestedInteger> stack = new ArrayDeque<>();
        NestedInteger res = new NestedInteger();
        stack.push(res);
        int left = 1, right = 1;

        for (; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (ch == '[') {
                NestedInteger nested = new NestedInteger();
                // 重置左指针的边界
                left = right + 1;
                // 当前nested对象 属于上一个nested，同时再入栈
                stack.peek().add(nested);
                stack.push(nested);
            } else if (ch == ']' || ch == ',') {
                // 处理数字，前提是左右边界成立
                if (left < right) {
                    Integer val = Integer.valueOf(s.substring(left, right));
                    // 加入到当前的nested对象中
                    stack.peek().add(new NestedInteger(val));
                }
                left = right + 1;
                if (ch == ']') stack.pop();
            }
        }

        return res;
    }
}

```



### 法二：逐个字符处理

```java
// 较为繁琐
class Solution {
    public NestedInteger deserialize(String s) {
        Stack<NestedInteger> stack = new Stack<>();
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }
        int op = 1;
        for (int i = 0; i < s.length();) {
            if (s.charAt(i) == '[') {
                stack.push(new NestedInteger());
                op = 1;
                i++;
            } else if (Character.isDigit(s.charAt(i))) {
                int num = s.charAt(i) - '0';
                i++;
                while (Character.isDigit(s.charAt(i))) {
                    num = num * 10 + s.charAt(i) - '0';
                    i++;
                }
                stack.peek().add(new NestedInteger(num * op));
            } else if (s.charAt(i) == '-') {
                op = -1;
                i++;
            } else if (s.charAt(i) == ',') {
                op = 1;
                i++;
            } else {
                if (stack.size() == 1) 
                    break;
                NestedInteger nest = stack.pop();
                stack.peek().add(nest);
                i++;
                op = 1;
            }
        }
        return stack.pop();
    }
}
```
