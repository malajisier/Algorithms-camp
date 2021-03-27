- 思路：
  - 既然pushed 数组是按一定顺序 push进去的，popped数组的弹出顺序也要对应起来   
  - 比如栈顶元素是3，同时对应位置的popped 下个弹出的元素也必须是2  


```java
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        if (pushed.length != popped.length) return false;

        int idx = 0;
        // 遍历pushed，存入辅助栈
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < pushed.length; i++) {
            stack.push(pushed[i]);
            
            // 先判断栈顶元素，是否是popped的第一个数字
            // 是的话，继续判断剩下的元素 是否可以都pop 
            while (!stack.isEmpty() && stack.peek() == popped[idx]) {
                stack.pop();
                idx++;
            }
        }

        return stack.isEmpty();
    }
}

```