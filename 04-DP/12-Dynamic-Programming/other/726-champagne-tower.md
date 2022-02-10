### dp  
- 时间：O(n^2)，空间：O(n^2)   
-   

```java
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] arr = new double[102][102];
        // 初始化第一杯
        arr[0][0] = poured;

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j <= i; j++) {
                // 当前杯子有溢出时
                if (arr[i][j] > 1.0) {
                    // 溢出量
                    double over = arr[i][j] - 1.0;
                    arr[i][j] = 1.0;
                    // 左下右下杯子 平分溢出量
                    arr[i + 1][j] += over / 2.0;
                    arr[i + 1][j + 1] += over / 2.0;
                }
            }
        }
        return arr[query_row][query_glass];
    }
}
```