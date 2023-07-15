
public class ReversedStrings {
    public static String RevString(String str) {
        
        String res =  "";
        for (int c = str.length()-1; c>=0; c--) {
            res += str.charAt(c);
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(RevString("Ola"));

    }
}
