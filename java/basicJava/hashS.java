
import java.util.HashSet;
public class hashS {
    public static void main(String[] args) {
        HashSet<String> list = new HashSet<String>();
        list.add("hello");
        list.add("how");
        list.add("are");
        list.add("you");
        System.out.println(list);
        list.remove("hello");
        System.out.println(list);
    }
}