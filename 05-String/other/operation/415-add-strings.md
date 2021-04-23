### 法一：双指针+补0
- 补0，有技巧性：指针为负数时补0，完美处理两个数字 位数不同时的情况
- 时间复杂度: O(max(len1, len2)), 空间：O(1)  

```java
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuffer res = new StringBuffer("");
        int i = num1.length() - 1, j = num2.length() - 1, carry = 0;

        while (i >= 0 || j >=0) {
            int n1 = i >= 0 ? num1.charAt(i) : 0;
            int n2 = j >= 0 ? num2.charAt(i) : 0;
            int tmp = n1 + n2 + carry;
            carry = tmp / 10;
            res.append(tmp % 10);
            i--;
            j--;
        }
        if (carry == 1) res.append(1);
        // 计算时是在末尾添加的，需要反转
        return res.reverse().toString();
    }
}

```


### 法二：直接模拟计算

``java

```