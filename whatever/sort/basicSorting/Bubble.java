package sort.basicSorting;

public class Bubble {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 3, 4, 6};
        bubbleSort(arr);

        System.out.println("정렬된 배열:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 인접한 두 원소를 비교하여 정렬 순서가 아니면 교환
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // 이번 패스에서 교환이 없었다면 배열이 이미 정렬되었다는 의미이므로 종료
            if (!swapped) {
                break;
            }
        }
    }
}
