import calc.mycalc;
import java.util.Scanner;

public class simplecalc{
    public static void main(String[] args) {
        Scanner myscan = new Scanner(System.in);

        System.out.println("Enter First Number:");
        int n1 = myscan.nextInt();
        System.out.println("Enter Second Number:");
        int n2 = myscan.nextInt();

        mycalc abc = new mycalc();

        System.out.println("Choose any one of the following options");
        System.out.println("1.Addition");
        System.out.println("2.Subtraction");
        System.out.println("3.Multiplication");
        System.out.println("4.Division");
        int option = myscan.nextInt();

        switch(option){
            case 1:
                abc.myadd(n1,n2);
                break;
            case 2:
                abc.mysub(n1,n2);
                break;
            case 3:
                abc.mymul(n1,n2);
                break;
            case 4:
                abc.mydiv(n1,n2);
                break;
            default:
                System.out.println("Invalid Entry");
        }


    }
}