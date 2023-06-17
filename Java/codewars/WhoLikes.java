package codewars;

public class WhoLikes {

    public static String WhoLikesIt(String[] names) {
        String pe = "";
        int c =0;
        if (names.length >= 4) {
             pe += names[0] + ", " + names[1] + " and " + (names.length-2) + " others ";
        }
        else if (names.length >= 1) {
            for (String i: names) {
                pe += i;
                if ((names.length == 2 && c == 0) || (names.length == 3 && c == 1)) {
                    pe += " and ";
                } else if (names.length == 3 && c == 0) {
                    pe += ", ";
                } else {
                    pe += " ";
                }
                c++;
            }
        }
        else if (names.length == 0) {
             pe += "no one ";
        }
        if (names.length >= 2) {
            return pe + "like this";
        } else {
            return pe + "likes this";
        }
        
    }

    public static void main(String[] args) {
        String[] array = {"Jacob","Alex", "Max", "Geremias"};
        System.out.println(WhoLikesIt(array));

    }
}
