
import java.util.*;
public class arlist1 {
    public static void main(String[] args) {
        ArrayList<String> data = new ArrayList<String>();
        data.add("hello");
        data.add("how");
        data.add("are");
        data.add("you");
        Iterator itr=data.iterator();  
        while(itr.hasNext()){
            System.out.println(itr.next()); 
        }
    }
}


