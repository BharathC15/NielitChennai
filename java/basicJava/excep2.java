
public class excep2 {
    public static void main(String[] args) {
        int age = -2;
        try {
            if (age <0){
                throw new ArithmeticException ("Age Cannot be negative");
            }
        } catch (ArithmeticException e){
            System.out.println(e);
            System.out.println("Resetting the Age Value");
            age = 0;
        }
        System.out.println("Age is "+age);
    }
}