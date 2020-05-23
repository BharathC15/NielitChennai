import java.util.Scanner;
public class fiboGen{
    public static void main(String[] args ){
        Scanner myscan = new Scanner(System.in);
        
        System.out.println("Enter the Upper limit :");
        int n = myscan.nextInt();

        int a = 0;
        int b = 1;
        int fib = 0;

        while ((a+b) <= n){
            fib = a + b;
            a = b;
            b = fib;
            System.out.println(fib);
        }

    }
}