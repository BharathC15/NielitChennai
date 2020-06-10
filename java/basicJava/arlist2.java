
import java.util.*;
public class arlist2 {
    public static void main(String[] args) {
        ArrayList<String> data = new ArrayList<String>();
        data.add("hello");
        data.add("how");
        data.add("are");
        data.add("you");
        System.out.println("2nd Element is "+data.get(1));

        data.set(1,"HOW");
        System.out.println(data);
    }
}


