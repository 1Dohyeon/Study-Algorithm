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
         * i-1 �� ��쿡���� ���η� �� Ÿ���� ���� ��� 1���� ����.
         * i-2 �� ��쿡���� ���η� �� Ÿ�� 2���� ���� ����
         * 2x2 ũ���� Ÿ���� ���� ��� �ΰ��� ��������.
         * ���⼭ ���η� �� Ÿ�� 2���� �ȳ��� ������ i-1�� ���� �ߺ��Ǳ� ����.*/
        for(int i=3; i<N+1; i++) {
            dp[i] = (2*dp[i-2] + dp[i-1])%10007;
        }

        return dp[N];
    }
}
