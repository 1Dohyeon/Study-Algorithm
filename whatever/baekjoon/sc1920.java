package baekjoon;

import java.util.Scanner;
import java.util.Arrays;

public class sc1920 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int[] arr = new int[N];


        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }

        Arrays.sort(arr);

        int M = in.nextInt();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < M; i++) {

            // ã���� �ϴ� ���� ���� ��� 1, ���� ��� 0�� ����ؾ��Ѵ�.
            if(binarySearch(arr, in.nextInt()) >= 0) {
                sb.append(1).append('\n');
            }
            else {
                sb.append(0).append('\n');
            }
        }
        System.out.println(sb);
    }


    /**
     * @param arr ���� �� �迭
     * @param value ã������ ��
     * @return key�� ��ġ�ϴ� �迭�� �ε���
     */
    public static int binarySearch(int[] arr, int value) {

        int lo = 0;					// Ž�� ������ ���� �� �ε���
        int hi = arr.length - 1;	// Ž�� ������ ������ �� �ε���

        // lo�� hi���� Ŀ���� ������ �ݺ��Ѵ�.
        while(lo <= hi) {

            int mid = (lo + hi) / 2;	// �߰���ġ�� ���Ѵ�.

            // key���� �߰� ��ġ�� ������ ���� ���
            if(value < arr[mid]) {
                hi = mid - 1;
            }
            // key���� �߰� ��ġ�� ������ Ŭ ���
            else if(value > arr[mid]) {
                lo = mid + 1;
            }
            // key���� �߰� ��ġ�� ���� ���� ���
            else {
                return mid;
            }
        }

        // ã���� �ϴ� ���� �������� ���� ���
        return -1;

    }
}