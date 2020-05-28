
class A {
    void display(){
        System.out.println("From Class A");
    }
}

class B extends A {
    void display(){
        System.out.println("From Class B");
    }
    void printMsg(){
        display();
        super.display(); // Super Keyword
    }
}

public class C extends B{
    public static void main(String args[]){
	    C obj = new C();
	    obj.printMsg();
    }
}



