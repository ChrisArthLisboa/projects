package codewars.fundamentos;

public class Greed {
    public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
        int sum = 0;
        for (int c = 0; c< classPoints.length; c++) {
            sum += classPoints[c];
        }
        if (yourPoints > sum/classPoints.length) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        int[] num = {1,2,3,4,5};
        System.out.println(betterThanAverage(num, 10));
    }
}
