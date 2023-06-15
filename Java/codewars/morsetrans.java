package codewars;

import java.util.ArrayList;

public class morsetrans {

  public static String decode(String morseCode) {
    int c=-1;
    morseCode = morseCode.strip();
    String[] array = String.valueOf(morseCode).split(" ");
    ArrayList<String> dec = new ArrayList<String>();
    for (String i: array) {
      if (i == null && dec.lastIndexOf(" ") != c) {
      	dec.add(" ");
      } else if (dec.lastIndexOf(" ") == c && c != -1) {
        dec.add("");
      } else {
        dec.add(i); 
      }
      c++;
    }
    dec.toArray();
    String strfin = String.join("", dec);
  	return strfin;
  }
}
