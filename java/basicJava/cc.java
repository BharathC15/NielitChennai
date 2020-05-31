
interface aa {
    public void f1(); // interface method
}

interface bb {
    public void f2(); // interface method
}

public class cc implements aa,bb {
    // Method overridding
    public void f1(){
        System.out.println("From F1");
    }
    public void f2(){
        System.out.println("From F2");
    }

    public static void main(String[] args) {
        cc obj= new cc();
        obj.f1();
        obj.f2();
    }
}

