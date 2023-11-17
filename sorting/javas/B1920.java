package baekjoon.Sorting;

import java.util.Scanner;
import java.util.Arrays;

public class B1920 {

    /**
     * BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

     int N = Integer.parseInt(br.readLine());
     int[] arr = new int[N];

     String[] input = br.readLine().split(" ");
     for (int i = 0; i < N; i++) {
     arr[i] = Integer.parseInt(input[i]);
     }

     // Arrays Ŭ���� ���� �ִ� sort(dual quick sort) �޼���� ����
     Arrays.sort(arr);

     int M = Integer.parseInt(br.readLine());
     input = br.readLine().split(" ");
     for (int i = 0; i < M; i++) {
     int target = Integer.parseInt(input[i]);
     System.out.println(binarySearch(arr, target, 0, arr.length - 1));
     }

     br.close();

     main�� �� �ڵ�ó�� bufferedreader�� �Է¹����� �� ����.*/

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // Arrays Ŭ���� ���� �ִ� sort(dual quick sort) �޼���� ����
        Arrays.sort(arr);

        int M = sc.nextInt();
        for(int i = 0; i < M; i++) {
            System.out.println(binarySearch(arr, sc.nextInt(), 0, arr.length - 1));
        }

        sc.close();
    }

    /** ����Ž������ �迭 arr�� start ~ end ���� ������ ã������ ��(value)�� ã��.*/
    public static int binarySearch(int[] arr, int value, int start, int end) {
        if (start <= end) {

            int mid = start + (end - start) / 2;

            if (arr[mid] == value) {
                return 1;
            }
            if (arr[mid] < value) {
                return binarySearch(arr, value, mid + 1, end);
            } else {
                return binarySearch(arr, value, start, mid - 1);
            }

        }
        return 0;
    }
}