有点没大理解题意  

参考题解：https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii/solution/shan-lie-zao-xu-by-yue-176/

```java
class Solution {
    public int minDeletionSize(String[] A) {
        int rows = A.length, cols = A[0].length();
        int[] vis = new int[rows];
       
        int counts = 0;
        for (int i = 0; i < cols; i++) {
            boolean isdel = false;
            for (int j = 1; j < rows; j++) {
                if (vis[j] == 1) continue;
                if (A[j].charAt(i) < A[j - 1].charAt(i)) {
                    isdel = true;
                    break;
                }
            }

            if (isdel) counts++;
            else {
                for (int k = 1; k < rows; k++) {
                    if (A[k].charAt(i) > A[k - 1].charAt(i)) {
                        vis[k] = 1;
                    }
                }
            }
        }

        return counts;
    }
}
```