
import java.util.PriorityQueue;
public class priQueue2 {
    public static void main(String[] args) {
        PriorityQueue<String> numbers = new PriorityQueue<String>();
        numbers.add("hello");
        numbers.add("how");
        numbers.add("are");
        numbers.add("you");
        while(!numbers.isEmpty()){
            System.out.println("Removed Element : "+numbers.remove());
        }
    }
}