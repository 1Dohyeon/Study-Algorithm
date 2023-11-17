package baekjoon.DynamicProgramming;

import java.util.Scanner;

public class B2579 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] stair = new int[n+1];

        for(int i=1; i<=n; i++) {
            stair[i] = sc.nextInt();
        }

        System.out.println(solution(stair, n));
        sc.close();
    }

    private static int solution(int[] arr, int stairSize) {
        int[] result = new int[stairSize+1];

        result[1] = arr[1];

        // n(stairSize)=1�� �Էµ� ��� arr[2]�� �������� �����Ƿ� ������ ���ٸ� ������ ��
        if(stairSize>=2) {
            result[2] = arr[1] + arr[2];
        }

        for(int i=3; i<=stairSize; i++) {
            result[i] = Math.max(result[i-2], arr[i-1] + result[i-3]) + arr[i];
        }

        return result[stairSize];
    }
}