package leetCode.DynamicProgramming;

public class SC1025DivisorGame {
    /**
     * n�� �־����� �� n�� ����� x�� ����.
     * n-x�� �� ���ڰ� ���� ���� ���ο� n�� �ȴ�.
     * �� ������ �ݺ��ؼ� �� �̻� ������ x�� ���ٸ� �й�*/
    public boolean divisorGame(int n) {
        // dp[i]�� ���� i���� ������ �������� �� Alice�� �̱� �� �ִ��� ��Ÿ���� �迭
        boolean[] dp = new boolean[n + 1];

        // dp[0], dp[1] �� �⺻�� false
        for (int i=2; i<=n; i++) {
            // Alice�� ���ʿ���, ������ ��� x�� ���� �˻�
            for (int x=1; x<i; x++) {
                // ���� x�� ���������� i-x���� Alice�� ���ٸ�,
                // Bob ���� �� ���ۿ� ���� => �� �� �ּ��� ���ϱ� ����.
                // ��, dp[i-x]�� false ��� dp[i]�� true �� �� ���ۿ� ����.
                if (i % x == 0 && !dp[i-x]) { // dp[i-x]==false ==> !dp[i-x]
                    dp[i] = true;
                    break; // �� �̻� �˻��� �ʿ� ����
                }
            }
        }

        return dp[n];
    }
}
