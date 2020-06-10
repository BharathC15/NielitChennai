
import java.util.*;
public class lnlist {
    public static void main(String[] args) {
        LinkedList<String> data=new LinkedList<String>();
        data.add("Hello");
        data.add("How");
        data.add("are");
        data.add("you");
        System.out.println("Data is \n"+data);

        System.out.println("First Element is \n"+data.getFirst());
        System.out.println("Last Element is \n"+data.getFirst());
        
        data.removeFirst();
        data.removeLast();
        
        data.addFirst("Hi");
        data.addLast("bye");
        System.out.println("Final Data \n"+data);
    }
}


