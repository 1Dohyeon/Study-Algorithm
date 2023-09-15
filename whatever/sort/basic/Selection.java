package sort.basic;

public class Selection {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 3, 4, 6};
        selectionSort(arr);

        System.out.println("정렬된 배열:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            // 현재 인덱스를 기준으로 최솟값을 찾음
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // 최솟값과 현재 인덱스의 원소를 교환
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}
