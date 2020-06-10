
import java.util.ArrayDeque;
public class arrayDq {
    public static void main(String[] args) {
        ArrayDeque<String> list = new ArrayDeque<String>();
        list.add("Hello");
        list.add("are");
        list.add("you");
        list.add("bye");
        System.out.println("Elements in the arrayDeque: "+list);
        System.out.println("Removed Last element: "+list.removeLast());
        System.out.println("Head :"+list.element());
    }
}