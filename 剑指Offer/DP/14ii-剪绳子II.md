- 新条件：大树越界的取余问题   
```
大数越界： 剪绳子问题（不考虑取余）最终的结果是以3^a的指数级别增长，可能超出 int32 甚至 int64 的取值范围，导致返回值错误
```
- 补充点：快速幂解，[链接](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/jian-dan-li-jie-kuai-su-mi-by-ollieq-rl74/)  


### 法一：dp
```java
import java.math.BigInteger;

class Solution {
    public int cuttingRope(int n) {
        BigInteger[] dp = new BigInteger[n + 1];
        Arrays.fill(dp, BigInteger.valueOf(1));
        for (int i = 3; i < n + 1; i++) {
            for (int j = 2; j < i; j++) {
                dp[i] = dp[i].max(BigInteger.valueOf(j * (i - j)).max(dp[i - j].multiply(BigInteger.valueOf(j))));
            }
        }
        return dp[n].mod(BigInteger.valueOf(1000000007)).intValue();
    }
}
```  


### 法二：快速幂解，最优方法     
- 时间：O(logn), 空间：O(1)   

```java
class Solution {
    int mod = 1000000007;
    public int cuttingRope(int n) {
        if(n < 4) return n - 1;
        int a = n / 3;
        int b = n % 3;
        if(b == 0) {
            return (int) (myPow(3, a) % mod);
        }
        else if(b == 1) {
            return (int) (myPow(3, a - 1) * 4 % mod);
        }
        else {
            return (int) (myPow(3, a) * 2 % mod);
        }
    }

    public long myPow(long base, int num){
        long res = 1;
        while(num > 0){
            if((num & 1) == 1){
                res *= base;
                res %= mod;
            }
            base *= base;
            base %= mod;
            num >>= 1;
        }
        return res;
    }
}
```