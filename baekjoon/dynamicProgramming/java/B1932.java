package baekjoon.DynamicProgramming;

import java.util.Scanner;

public class B1932 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] tree = new int[n][n];

        for (int i=0; i<n; i++) {
            for(int j=0; j<=i; j++) {
                tree[i][j] = scanner.nextInt();
            }
        }

        System.out.println(solution(tree, n));
    }

    private static int solution(int[][] arr, int n) {
        int[][] dp = new int[n][n];
        dp[0][0] = arr[0][0];

        for (int i=1; i<n; i++){
            for(int j=0; j<n; j++) {
                if(j==0) {
                    dp[i][j] = dp[i-1][j] + arr[i][j];
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j];
                }
            }
        }

        int result=0;
        // 마지막인 맨 아래층에서 각각에 최댓값을 가지고 있기 때문에 이곳에서 가장 큰 값 찾아준다.
        for(int i=0; i<n; i++) {
            if(result < dp[n-1][i]) result = dp[n-1][i];
        }

        return result;
    }
}
