
import java.util.*;  
public class vecExample{  
    public static void main(String args[]){  
        Vector<String> v=new Vector<String>();  
        v.add("Hello");  
        v.add("How");  
        v.add("Are");  
        v.add("You");  
        Iterator<String> itr=v.iterator();  
        while(itr.hasNext()){  
            System.out.println(itr.next());  
        }  
    }  
}  


