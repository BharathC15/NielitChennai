import java.util.Scanner;
import java.util.ArrayList;
public class calcAdv {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> history = new ArrayList<>();
        System.out.println("Welcome to my Calculator!!");
        boolean flag = true;
        int userOption,op1,op2,result;
        String testing;
        System.out.println("Press 1 : For Addition");
        System.out.println("Press 2 : For Subtraction");
        System.out.println("Press 3 : For Multiplication");
        System.out.println("Press 4 : For Division");
        System.out.println("Press 9 : To Display History");
        System.out.println("Press 0 : To Exit this program");
        while(flag){
            System.out.println("Select an option from above :");
            System.out.println("Your option:");
            userOption = scan.nextInt();
            switch(userOption){
                case 1 :
                System.out.println("Enter the first Operand :");
                op1 = scan.nextInt();
                System.out.println("Enter the second Operand :");
                op2 = scan.nextInt();
                System.out.println("Answer is :");
                result = op1 + op2;
                testing = op1+"+"+op2+"="+result;
                System.out.println(testing);
                history.add(testing);
                System.out.println(" ");
                break;

                case 2 :
                System.out.println("Enter the first Operand :");
                op1 = scan.nextInt();
                System.out.println("Enter the second Operand :");
                op2 = scan.nextInt();
                System.out.println("Answer is :");
                result = op1 - op2;
                testing = op1+"-"+op2+"="+result;
                System.out.println(testing);
                history.add(testing);
                System.out.println(" ");
                break;

                case 3 :
                System.out.println("Enter the first Operand :");
                op1 = scan.nextInt();
                System.out.println("Enter the second Operand :");
                op2 = scan.nextInt();
                System.out.println("Answer is :");
                result = op1 * op2;
                testing = op1+"*"+op2+"="+result;
                System.out.println(testing);
                history.add(testing);
                System.out.println(" ");
                break;

                case 4 :
                System.out.println("Enter the first Operand :");
                op1 = scan.nextInt();
                System.out.println("Enter the second Operand :");
                op2 = scan.nextInt();
                System.out.println("Answer is :");
                result = op1 / op2;
                testing = op1+"/"+op2+"="+result;
                System.out.println(testing);
                history.add(testing);
                System.out.println(" ");
                break;

                case 9:
                for(String str:history){
                    System.out.println(str);
                }
                System.out.println(" ");
                break;

                case 0 :
                System.out.println("Thank you");
                flag=false;
                break;

                default:
                System.out.println("Invalid entry \nTry Again !!");
                System.out.println(" ");

            }
        }
        scan.close();
    }
}