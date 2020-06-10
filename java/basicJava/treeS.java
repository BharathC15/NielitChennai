
import java.util.TreeSet;
import java.util.Random;
public class treeS {
    public static void main(String[] args) {
        Random rand = new Random(); 
        TreeSet<Integer> num = new TreeSet<Integer>();
        for(int i=0;i<50;i++){
            num.add(rand.nextInt(100));
        }
        System.out.println(num);
        TreeSet<Integer> newNum = (TreeSet<Integer>) num.subSet(25, 50);
        System.out.println("Subset of Random Numbers \n"+newNum);
    }
}