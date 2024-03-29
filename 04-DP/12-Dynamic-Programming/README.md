## 动态规划
### 1. basic     
区别   
- 与递归、分治没有根本上的区别，关键看有无最优子结构
- 共同点：找到重复子问题
- 不同点：DP中的最优子结构，并且中途可以淘汰次优解

关键点：
- 1.最优子结构
  - optimal = best_of(opt[n - 1], opt[n - 2])
- 2.存储中间状态：opt[i]
- 3.递推公式（状态转移方程 或 DP方程）
  - 斐波那契数列： opt[i] = opt[n - 1] + opt[n - 2]
  - 二维路径(62, 63)： opt[i, j] = opt[i + 1][j] + opt[i][j + 1]，判断a[i, j]是否为空地        

解题步骤：
- 1.子问题
- 2.状态定义
- 3.DP方程         
          


### 2. 题目分类  
#### 2.1 背包问题及变种



#### 经典类型   
买卖股票
- 121-买卖股票的最佳时机：股票的最大利润：最多1笔交易
- 122-买卖股票的最佳时机 II：尽可能更多次的交易
- 123-买卖股票的最佳时机 III：2笔交易
- 188-买卖股票的最佳时机 IV：最多k笔交易
- 309-最佳买卖股票时机含冷冻期：与122题的区别是卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
- 714-买卖股票的最佳时机含手续费：与122题的区别是每笔交易都需要付手续费

打家劫舍    






