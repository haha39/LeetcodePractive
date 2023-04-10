import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class sol {
    public static void main(String[] args) {

        int[] groupSizes = { 3, 3, 3, 3, 3, 1, 3 };
        System.out.println(groupThePeople(groupSizes));
    }

    public static List<List<Integer>> groupThePeople(int[] groupSizes) {

        List<List<Integer>> output = new ArrayList<List<Integer>>();
        List<Integer> a = new ArrayList<Integer>();
        a.add(0);
        a.add(1);
        List<Integer> b = new ArrayList<Integer>();
        b.add(3);
        output.add(a);
        output.add(b);

        int len = groupSizes.length;

        System.out.println(output.size());
        System.out.println(groupSizes.length);

        Arrays.sort(groupSizes);

        for (int i : groupSizes) {
            System.out.print(i + "  ");
        }
        System.out.println();

        for (int i = 0; i < len; i++) {
            int index = 0;

            for (int j = 0; j < groupSizes[i]; j++) {

                // i += groupSizes[i];
            }

        }

        return output;
    }

}
