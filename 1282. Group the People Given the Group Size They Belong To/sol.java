import java.util.ArrayList;
//import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class sol {
    public static void main(String[] args) {

        int[] groupSizes = { 3, 3, 3, 3, 3, 1, 3 };
        System.out.println(groupThePeople(groupSizes));
    }

    public static List<List<Integer>> groupThePeople(int[] groupSizes) {

        List<List<Integer>> output = new ArrayList<List<Integer>>();
        // List<Integer> a = new ArrayList<Integer>();
        // a.add(0);
        // a.add(1);
        // List<Integer> b = new ArrayList<Integer>();
        // b.add(3);
        // output.add(a);
        // output.add(b);

        int len = groupSizes.length;

        System.out.println(output.size());
        System.out.println(groupSizes.length);

        Map<Integer, Integer> groupSizesMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < len; i++) {
            groupSizesMap.put(i, groupSizes[i]);
        }

        List<Entry<Integer, Integer>> list = new ArrayList<>(groupSizesMap.entrySet());
        list.sort(Entry.comparingByValue());
        list.forEach(System.out::println);
        // groupSizesMap = sortByKeys(groupSizesMap);

        for (int i = 0; i < len; i++) {
            System.out.print(list.get(i).getKey() + "  ");
            System.out.print(list.get(i).getValue());
            System.out.println();
        }
        System.out.println();

        int index = 0;

        while (index < len) {

            List<Integer> list_tmp = new ArrayList<Integer>();
            int size = list.get(index).getValue();

            System.out.println(index);
            System.out.println(size);

            for (int j = 0; j < size; j++) {
                int index_tmp = list.get(index + j).getKey();
                System.out.print("    " + index_tmp + "    ");

                list_tmp.add(index_tmp);
            }
            System.out.println();
            index += size;
            output.add(list_tmp);
            System.out.println(index);
            System.out.println();

        }

        return output;
    }

}
