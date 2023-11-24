package Sort.basicSorting;

public class Insertion {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 3, 4, 6};
        insertionSort(arr);

        System.out.println("정렬된 배열:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void insertionSort(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            // key를 적절한 위치에 삽입
            // ex) {2, 5, 9, 3, 4, 6}
            //               i:3
            //      2 <- j:9
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }
}
