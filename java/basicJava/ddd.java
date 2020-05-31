
interface aaa {
    public void f1();
}
interface bbb extends aaa{
    public void f2();
}
interface ccc {
    public void f3();
}

public class ddd implements bbb,ccc {
    // Method overridding
    public void f1(){
        System.out.println("From AAA");
    }
    public void f2(){
        System.out.println("From BBB");
    }
    public void f3(){
        System.out.println("From CCC");
    }
    public void f4(){
        System.out.println("From DDD");
    }

    public static void main(String[] args) {
        ddd obj= new ddd();
        obj.f1();
        obj.f2();
        obj.f3();
        obj.f4();

    }
}
