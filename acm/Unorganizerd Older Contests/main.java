import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numCases = sc.nextInt();

        int casesCovered = 0;

        while (casesCovered < numCases){
            int plats = sc.nextInt();
            int baller = sc.nextInt();
            int monyMade = 0;

            ArrayList<Integer> prices = new ArrayList<>();
            for(int i = 0; i < plats; i++){
                prices.add(sc.nextInt());
            }
            ArrayList<Integer> sold = new ArrayList<>();
            for(int i = 0; i < plats; i++){
                monyMade += sc.nextInt() * prices.get(i);
            }
            if(monyMade >= baller){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }

            casesCovered++;
        }
        while (sc.hasNext()){
            String i = sc.next();
        }
    }
}
