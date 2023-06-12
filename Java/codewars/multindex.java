package codewars;

import java.util.ArrayList;

public class multindex {
  public static ArrayList<Float> multipleOfIndex(float[] array) {
    ArrayList<Float> end = new ArrayList<Float>();
    for (int i=1;i<=array.length-1;i++) {
      int result = Math.round(array[i]/i);
        if (array[i]/i == result) {
            end.add(array[i]);
    	}
    }
    return end;
  }
  public static void main(String[] args) {
    float[] array = {22, -6, 32, 82, 9, 25};
    System.out.println(multipleOfIndex(array));

  }
}
