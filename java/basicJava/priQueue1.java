
import java.util.PriorityQueue;
public class priQueue1 {
    public static void main(String[] args) {
        PriorityQueue<Integer> numbers = new PriorityQueue<Integer>();
        numbers.add(256);
        numbers.add(12);
        numbers.add(8);
        numbers.add(512);
        numbers.add(1024);
        while(!numbers.isEmpty()){
            System.out.println("Removed Element : "+numbers.remove());
        }
    }
}