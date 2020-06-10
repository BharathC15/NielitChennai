
import java.util.*;
public class arlist3 {
    public static void main(String[] args) {
        ArrayList<String> data = new ArrayList<String>();
        data.add("hello");
        data.add("how");
        data.add("are");
        data.add("you");
        Collections.sort(data);
        System.out.println(data);
    }
}


