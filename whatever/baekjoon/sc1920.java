package baekjoon;

import java.util.Scanner;
import java.util.Arrays;

public class sc1920 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // Arrays 클래스 내에 있는 sort(dual quick sort) 메서드로 정렬
        Arrays.sort(arr);

        int M = sc.nextInt();
        for(int i = 0; i < M; i++) {
            System.out.println(binarySearch(arr, sc.nextInt(), 0, arr.length - 1));
        }

        sc.close();

        /**
         * BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

         int N = Integer.parseInt(br.readLine());
         int[] arr = new int[N];

         String[] input = br.readLine().split(" ");
         for (int i = 0; i < N; i++) {
         arr[i] = Integer.parseInt(input[i]);
         }

         // Arrays 클래스 내에 있는 sort(dual quick sort) 메서드로 정렬
         Arrays.sort(arr);

         int M = Integer.parseInt(br.readLine());
         input = br.readLine().split(" ");
         for (int i = 0; i < M; i++) {
         int target = Integer.parseInt(input[i]);
         System.out.println(binarySearch(arr, target, 0, arr.length - 1));
         }

         br.close();

         main에 위 코드처럼 bufferedreader로 입력받으면 더 빠름.*/
    }

    /** arr의 start ~ end 범위에서 value가 있는지 재귀 호출을 이용하여 이진탐색으로 찾음.*/
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