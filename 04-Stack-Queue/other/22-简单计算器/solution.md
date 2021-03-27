```java
class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new LinkedList<>();
        // res 存实时计算的结果，sign 正负号
        int res = 0, n = s.length(), sign = 1;

        for (int i = 0; i < n; i++) {
            int num = 0; 
            if (s.charAt(i) >= '0') {
                // 连续数字计算
                while (i < n && s.charAt(i) >= '0') {
                    // 直接使用ASCII码相减
                    num = num * 10 + (s.charAt(i) - '0');
                    i++; 
                }
                i--;
                res += sign * num;
            } else if (s.charAt(i) == '+') {
                sign = 1;
            } else if (s.charAt(i) == '-') {
                sign = -1;
            
            // 遇到左括号，就把之前的结果和正负号存储 
            } else if (s.charAt(i) == '(') {
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            } else if (s.charAt(i) == ')') {
                res *= stack.peek();
                stack.pop();
                res += stack.peek();
                stack.pop();
            }   
        }

        return res;
    }
}

// 输入"(4+(5+2)-3)"， 模拟一遍
// st=(0,1)
// num=4,res=4
// st=(0,1,4,1), res=0
// res=5,num=2,res=7
// res=7, st.pop(1)
// res=7+4=11,st.pop(4)
// res=11-3=7

```