
public class Animal {
    int legs;

    public Animal(int n){
        legs = n;
    }
    
    public static void main(String[] args) {
        Animal Lion = new Animal(4);
        Animal Human = new Animal(2);

        System.out.println(Lion.legs); // Output 4
        System.out.println(Human.legs); // Output 2
    }
} 

