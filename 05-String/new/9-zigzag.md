### 法一：根据过程模拟   

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() == 1) {
            return s;
        }

        // 初始化每一行
        StringBuilder[] res = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            res[i] = new StringBuilder();
        }
        
        int index = 0;  // 每个字符的索引
        int row = 0;
        int n = s.length();
        while (index < n) {
            // 竖着每一行添加
            while (index < n && row < numRows) {
                char ch = s.charAt(index++); // index，row也需要增加
                res[row++].append(ch);
            }
            
            // 一定要判断index 是否越界 
            if (index == n) break;

            // row在最后一行，作为索引比numRows小1，所以到倒数第二行需要+2
            row = numRows - 2;
            while (index < n && row >= 0) {
                char ch = s.charAt(index++);
                res[row--].append(ch);  
            }
            // 上面在添加完第0行之后(row=0)，row已经等于-1，row到第二行需要+2
            row += 2;
        }

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            ans.append(res[i]);
        }
        return ans.toString();
    }
}
```  


### 法二：使用flag，改变索引的上升或下降   

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() == 1) {
            return s;
        }
        List<StringBuilder> rows = new ArrayList<StringBuilder>();
        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }

        // p 指向当前行
        int p = 0, flag = -1;
        for (char ch : s.toCharArray()) {
            rows.get(p).append(ch);
            // p 说明在第一行或最后一行，需要变为下降或上升
            if (p == 0 || p == numRows - 1) flag = -flag;
            p += flag;
        }

        StringBuilder res = new StringBuilder();
        for (StringBuilder row : rows) {
            res.append(row);
        }
        return res.toString();
    }
}
```

