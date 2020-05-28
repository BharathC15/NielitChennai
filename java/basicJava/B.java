
class A {
    String str1 = "Hello";
}

public class B extends A{
    String str2 = "Hi";
    public static void main(String args[]){
	    B obj = new B();
	    System.out.println(obj.str1);
        System.out.println(obj.str2);
    }
}



