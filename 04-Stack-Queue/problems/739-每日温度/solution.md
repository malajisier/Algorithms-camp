```java
class Solution {
    public int[] dailyTemperatures(int[] T) {
        int n = T.length;
        int[] res = new int[n];
        // 存索引的单调栈，保持温度递减
        Deque<Integer> stack = new LinkedList<Integer>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && T[i] > T[stack.peek()]) {
                // 计算当前温度，与栈顶的索引的差值，依次出栈
                int preIdx = stack.pop();
                res[preIdx] = i - preIdx;
            }
            stack.push(i);
        }

        return res;
    }
}
```


