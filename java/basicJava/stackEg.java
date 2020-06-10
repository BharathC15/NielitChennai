
import java.util.*;  
public class stackEg{  
    public static void main(String args[]){  
        Stack<String> s=new Stack<String>();  
        s.push("Hello");  
        s.push("How");  
        s.push("Are");  
        s.push("You");  
        Iterator<String> itr=s.iterator();  
        while(itr.hasNext()){  
            System.out.println(itr.next());  
        }  
        s.pop();
        s.pop();
        System.out.println("After Twice pop : "+s);
        System.out.println("Peek output : "+s.peek());

    }  
}  


