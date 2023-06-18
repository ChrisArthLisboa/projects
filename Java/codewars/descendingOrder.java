package codewars;

import java.util.Arrays;
import java.util.Collections;

public class descendingOrder {
    public static int ordDesc(final int num) {
        String[] anum = String.valueOf(num).split("");
        Arrays.sort(anum, Collections.reverseOrder());
        
        return Integer.valueOf(String.join("", anum));
    }
    public static void main(String[] args) {
        System.out.println(ordDesc(12));
    }
}