
public class enumEg {
        // Create an enum
        enum Level {
            LOW,
            MEDIUM,
            HIGH
        }
  public static void main(String[] args) {
    // Print only Medium
    Level myVar = Level.MEDIUM; 
    System.out.println(myVar+"\n");

    // Loop through all elements in Level enum
    for (Level myVar1 : Level.values()) {
        System.out.println(myVar1);
    }
  }
}


