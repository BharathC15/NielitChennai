
import java.util.LinkedHashSet;
public class linkedhashS {
    public static void main(String[] args) {
        LinkedHashSet<String> list = new LinkedHashSet<String>();
        list.add("hello");
        list.add("how");
        list.add("are");
        list.add("you");
        list.add("hello");
        System.out.println(list);
        list.remove("hello");
        System.out.println(list);
    }
}