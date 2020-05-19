import java.util.Scanner;

class userAge {
    public static void main(String[] args) {
        Scanner myscan = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter username :");
        String userName = myscan.nextLine();
        
        System.out.println("Enter your Age :");
        int userAge = myscan.nextInt();

        System.out.println("Username is:"+userName.toUpperCase());
        System.out.println("User's half age is :" + (userAge/2));
    }
}