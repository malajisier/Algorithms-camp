public class Fibonacci {
    int fib1(int n, int[] memo) {
        if (0 == n || 1 == n) {return n;}
        if (memo[n] != 0) {return memo[n];}
        
        if (n > 1) {
            memo[n] = fib1(n - 1, memo) + fib1(n - 2, memo);
            return memo[n];
        }
        return 0;
    }
}
