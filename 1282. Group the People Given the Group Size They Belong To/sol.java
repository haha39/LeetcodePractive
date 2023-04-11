/*
 * Input: groupSizes = [3,3,3,3,3,1,3]
 *Output: [[5],[0,1,2],[3,4,6]]
 *Explanation: 
 *The first group is [5]. The size is 1, and groupSizes[5] = 1.
 *The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
 *The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
 *Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class sol {
    public static void main(String[] args) {

        // input
        int[] groupSizes = { 3, 3, 3, 3, 3, 1, 3 };

        System.out.println(groupThePeople(groupSizes));

    }

    public static List<List<Integer>> groupThePeople(int[] groupSizes) {

        int index = 0;
        int len = groupSizes.length;
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        Map<Integer, Integer> groupSizesMap = new HashMap<Integer, Integer>();

        // turn groupSizes into groupSizesMap(index, groupSizes[index])
        for (int i = 0; i < len; i++) {
            groupSizesMap.put(i, groupSizes[i]);
        }

        // sort by value!
        List<Entry<Integer, Integer>> list = new ArrayList<>(groupSizesMap.entrySet());
        list.sort(Entry.comparingByValue());
        // list.forEach(System.out::println);

        // group the people by their wanted size
        while (index < len) {

            List<Integer> list_tmp = new ArrayList<Integer>();
            int size = list.get(index).getValue();

            for (int j = 0; j < size; j++) {
                int index_tmp = list.get(index + j).getKey();
                list_tmp.add(index_tmp);
            }

            index += size;
            output.add(list_tmp);
        }

        return output;
    }

}
