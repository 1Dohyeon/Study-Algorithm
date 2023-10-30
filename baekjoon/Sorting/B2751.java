package baekjoon.Sorting;

import java.util.Scanner;

public class B2751 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }

        quickSort(arr, 0, N-1);

        for (int i : arr) {
            System.out.println(i);
        }

    }

    public static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            // �߾Ӱ��� �߾Ӱ��� �ǹ����� ����
            int pivotIndex = getPivotIndex(array, low, high);
            // �ǹ��� �������� ���� ���� �������� ū ���� ���������� �̵���Ŵ
            int partitionIndex = partition(array, low, high, pivotIndex);
            // ��Ƽ���� ���� �κа� ������ �κ��� ��������� ����
            quickSort(array, low, partitionIndex - 1);
            quickSort(array, partitionIndex + 1, high);
        }
    }

    public static int getPivotIndex(int[] array, int low, int high) {
        // �迭�� 5���� ������ �߾Ӱ��� ã��
        int n = high - low + 1;
        int[] medians = new int[(n + 4) / 5];
        for (int i = 0; i < medians.length; i++) {
            int start = low + i * 5;
            int end = Math.min(low + i * 5 + 4, high);
            insertionSort(array, start, end);
            medians[i] = array[start + (end - start) / 2];
        }
        // �߾Ӱ� �迭���� ��������� �߾Ӱ��� ã��
        return (medians.length == 1) ? medians[0] : getPivotIndex(medians, 0, medians.length - 1);
    }

    public static void insertionSort(int[] array, int low, int high) {
        for (int i = low + 1; i <= high; i++) {
            int key = array[i];
            int j = i - 1;
            while (j >= low && array[j] > key) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }

    public static int partition(int[] array, int low, int high, int pivotValue) {
        for (int i = low; i <= high; i++) {
            if (array[i] == pivotValue) {
                swap(array, i, high); // �ǹ��� �� ������ �̵�
                break;
            }
        }
        int pivotIndex = low;
        for (int i = low; i < high; i++) {
            if (array[i] <= pivotValue) {
                swap(array, i, pivotIndex);
                pivotIndex++;
            }
        }
        swap(array, pivotIndex, high); // �ǹ��� �ùٸ� ��ġ�� �̵�
        return pivotIndex;
    }

    public static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
