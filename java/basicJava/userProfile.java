import java.util.Scanner;
public class userProfile {
    String name;
    String age;

    public userProfile(String n,String a){
        name = n;
        age = a;
    }

    void userInfo() {
    System.out.println("Name of the user is "+name);
    System.out.println("Age of the user is "+age);
  }
    
    public static void main(String[] args) {
        Scanner myscan = new Scanner(System.in);

        System.out.println("Enter the name of user 1:");
        String n1 = myscan.nextLine();
        System.out.println("Enter the age of user 1:");
        String a1 = myscan.nextLine();

        System.out.println("Enter the name of user 2:");
        String n2 = myscan.nextLine();
        System.out.println("Enter the age of user 2:");
        String a2 = myscan.nextLine();
        
        userProfile user1 = new userProfile(n1,a1);
        userProfile user2 = new userProfile(n2,a2);

        System.out.println("User1 Information");
        user1.userInfo();
        System.out.println("User2 Information");
        user2.userInfo();
    }

}