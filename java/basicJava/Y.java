
class X {
    int num = 5;
}

public class Y extends X {
    int num = 10;
    void printNumber(){
        // Super keyword
        System.out.println(super.num);
    }
    public static void main(String args[]){
        Y obj= new Y();
	    obj.printNumber();	
   }
}