package baekjoon.DynamicProgramming;

import java.util.Scanner;

public class B11727 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        System.out.println(solution(n));
        sc.close();
    }

    private static int solution(int N) {
        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 3;

        /**
         * i-1 인 경우에서는 세로로 긴 타일을 놓는 경우 1개만 허용됨.
         * i-2 인 경우에서는 가로로 긴 타일 2개를 놓는 경우와
         * 2x2 크기의 타일을 놓는 경우 두개로 나뉘어짐.
         * 여기서 세로로 긴 타일 2개를 안놓는 이유는 i-1의 경우와 중복되기 때문.*/
        for(int i=3; i<N+1; i++) {
            dp[i] = (2*dp[i-2] + dp[i-1])%10007;
        }

        return dp[N];
    }
}
