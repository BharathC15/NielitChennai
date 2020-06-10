
import java.util.PriorityQueue;
import java.util.Comparator;
public class priQueue3 {
    public static void main(String[] args) {
        Comparator<String> myComp = new Comparator<String>(){
            public int compare(String s1, String s2){
                return (s1.length()-s2.length());
            }
        };
        PriorityQueue<String> names = new PriorityQueue<String>(myComp);
        names.add("abcde");
        names.add("aaaa");
        names.add("x");
        names.add("bye");
        while(!names.isEmpty()){
            System.out.println("Removed Element : "+names.remove());
        }
    }
}