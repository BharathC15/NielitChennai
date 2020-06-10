
public class excep1 {
    public static void main(String[] args) {
        int num1 = 1;
        int num2 = 0;
        try {
            int answer = num1 / num2;
        } 
        catch (ArithmeticException e){
            System.out.println("Arithmetic Exception Occured \n"+e);
        }
        catch (Exception e) {
            System.out.println("Unknown Exception Occured \n"+e);
        }
        finally {
            System.out.println("End of the Program");
        }
    }
}