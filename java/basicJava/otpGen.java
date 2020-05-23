import java.util.Scanner;
import java.util.Random;
public class otpGen{
    static String otp(int len){
        String randBha="";
        Random rand = new Random();

        for (int i = 0; i < len; i++){
            randBha=randBha+rand.nextInt(9);
        }
        return randBha;
    }
    public static void main(String[] bharath){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number of users:");
        int n = scan.nextInt();
        System.out.println("Enter the length of the OTP:");
        int l = scan.nextInt();

        for(int j=0;j<n;j++){
            System.out.println("OTP for user"+(j+1)+" is :"+otp(l));
        }
    }
}