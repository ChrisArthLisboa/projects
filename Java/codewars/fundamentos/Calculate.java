public class Calculate {
    public static String bmi(double weight, double height) {
        double res = weight/(height*height);
        String last = "";
        if (res <= 18.5) {
            last = "Underweight";
        } else if (res <= 25) {
            last = "Normal";
        } else if (res <= 30) {
            last = "Overweight";
        } else if (res > 30) {
            last = "Obese";
        }
        return last;
    }

    public static void main(String[] args) {
        System.out.println(bmi(80, 1.80));
    }
}
