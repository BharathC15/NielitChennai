package calc;

public class mycalc{
    public void myadd(int a,int b){
        System.out.println("The Addition of "+a+" and "+b+" is "+(a+b));
    }
    public void mysub(int a,int b){
        System.out.println("The Subtraction of "+a+" and "+b+" is "+(a-b));
    }
    public void mymul(int a,int b){
        System.out.println("The Multiplication of "+a+" and "+b+" is "+(a*b));
    }
    public void mydiv(int a,int b){
        if (b==0){
            System.out.println("Division by zero Not Possible");
        } else {
            System.out.println("The Division of "+a+" and "+b+" is "+(a/b));
        }
    }
}