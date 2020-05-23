import java.util.Scanner;
public class primeCheck{
    public static void main(String[] args ){
        Scanner myscan = new Scanner(System.in);
        
        System.out.println("Enter a number :");
        int l = myscan.nextInt();

        boolean flag = false; 

        for (int j = 2; j <= l/2 ; j++){
            if ( l % j == 0){
                flag = true;
                break;
            }
        }

        if (flag == false){
            System.out.println(l+": is a Prime Number ");
        } else {
            System.out.println(l+": is not a Prime Number");
        }

    }

}
