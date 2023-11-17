package leetCode.DynamicProgramming;

public class SC509FibonacciNumber {

    // 다이나믹 프로그래밍
    public int fib(int n) {
        if(n<=1) {
            return n;
        } else {
            int[] dp = new int[n+1];
            dp[1] = 1;
            for(int i=2; i<n+1; i++) {
                dp[i] = dp[i-2] + dp[i-1];
            }
            return dp[n];
        }
    }
    
    // 재귀함수
    public int fib2(int n) {
        if (n <= 2) {
            return 1;
        } else {
            return fib2(n - 1) + fib2(n - 2);
        }
    }
}
