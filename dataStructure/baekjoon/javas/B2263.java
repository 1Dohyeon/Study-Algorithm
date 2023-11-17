package baekjoon.Tree;

import java.util.Scanner;

public class B2263 {
    static StringBuffer sb = new StringBuffer();
    static int[] inorder;
    static int[] postorder;
    static int[] index;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        inorder = new int[n];
        postorder = new int[n];
        index = new int[n + 1];

        for (int i = 0; i < n; i++) {
            inorder[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            postorder[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            index[inorder[i]] = i;
        }

        PreOrder(0, n - 1, 0, n - 1);
        System.out.println(sb);

        sc.close();
    }

    public static void PreOrder(int inStart, int inEnd, int postStart, int postEnd) {
        if (inStart > inEnd || postStart > postEnd) {
            return;
        }

        int root = postorder[postEnd];
        sb.append(root).append(" ");

        int rootIndex = index[root];
        int leftSize = rootIndex - inStart;

        PreOrder(inStart, rootIndex - 1, postStart, postStart + leftSize - 1);

        PreOrder(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1);
    }
}
