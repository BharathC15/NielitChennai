import java.util.Scanner;
public class nMinMax{
    public static void main(String[] args ){
        Scanner myscan = new Scanner(System.in);
        
        int temp,min,max;
        int sum = 0;

        System.out.println("Enter the number of Terms :");
        int n = myscan.nextInt();

        System.out.println("Enter term 1 value:");
        temp = myscan.nextInt();
        min = temp;
        max = temp;
        sum += temp;

        for (int i=1;i<n;i++){
            System.out.println("Enter term "+(i+1)+" value:");
            temp = myscan.nextInt();

            sum +=temp;

            if (temp<min){
                min = temp;
            } else if (temp>max){
                max = temp;
            }
        }
        System.out.println("The Minimum value is :"+min);
        System.out.println("The Maximum value is :"+max);
        System.out.println("The Mean value is :"+(sum/n));
    }
}