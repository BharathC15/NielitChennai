import java.util.Scanner;
public class fiboPrime{
    public static void main(String[] args ){
        Scanner myscan = new Scanner(System.in);
        
        System.out.println("Enter the Upper limit :");
        int n = myscan.nextInt();

        System.out.println("Fibonacci Numbers which are Prime");

        int a = 0;
        int b = 1;
        int fib = 0;

        while ((a+b) <= n){
            fib = a + b;
            a = b;
            b = fib;
            if(fib>1){
                boolean flag = false; 

                for (int j = 2; j <= fib/2 ; j++){
                    if ( fib % j == 0){
                        flag = true;
                        break;
                    }
                }

                if (flag == false){
                    System.out.println(fib);
                } 
            }
        }

    }
}