package baekjoon;

public class sc2820 {
    static int numberCount = 2;
    class Node {
        int money;

        int number;
        int bossNumber;

        public Node(int money) {
            this.money = money;
            number = 1;
        }

        public Node(int money, int bossNumber) {
            this.money = money;
            this.bossNumber = bossNumber;
            number = numberCount;
            numberCount += 1;
        }

    }
}
