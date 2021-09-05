
### 法二：桶排序   

```java
class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int maxFreq = 0;
        int length = s.length();

        // 统计每个字符的出现次数
        for (int i = 0; i < length; i++) {
            char ch = s.charAt(i);
            int freq = map.getOrDefault(ch, 0) + 1;
            map.put(ch, freq);
            maxFreq = Math.max(maxFreq, freq);
        }

        StringBuffer[] buckets = new StringBuffer[maxFreq + 1];
        for (int i = 0; i <= maxFreq; i++) {
            buckets[i] = new StringBuffer();
        }
        // 根据map，按freq 统计字符
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            char key = entry.getKey();
            int freq = entry.getValue();
            buckets[freq].append(key);
        }

        StringBuffer res = new StringBuffer();
        for (int i = maxFreq; i > 0; i--) {
            // 当前频率的所有字符
            StringBuffer bucket = buckets[i];
            int size = bucket.length();
            // 遍历每个字符
            for (int j = 0; j < size; j++) {
                // 需要重复，添加freq个字符
                for (int k = 0; k < i; k++) {
                    res.append(bucket.charAt(j));
                }
            }
        }
        return res.toString();
    }
}
```







// 快排解法
class Solution {
    public String frequencySort(String s) {
        int[] counts = new int[128];
        char[] chars = s.toCharArray();
        for (char c : chars) {
            ++counts[c];
        }
        int[][]countArr = new int[128][];
        int index = 0;
        for (int i = 0; i < 128; ++i) {
            if (counts[i] > 0) {
                countArr[index++] = new int[]{counts[i], i};
            }
        }
        int resIndex = 0;
        quickSort(countArr, 0, index - 1);
        for (int i  = 0; i < index; ++i) {
            char c = (char) countArr[i][1];
            for (int j = 0; j < countArr[i][0]; ++j) {
                chars[resIndex++] = c;
            }
        }
        return new String(chars);
    }

    private void quickSort(int[][] arrs, int left, int right) {
        if (left >= right) {
            return;
        }
        swap(arrs, left, (left + right) >> 1);
        int index = left;
        for (int i = left + 1; i <= right; ++i) {
            if (arrs[i][0] >= arrs[left][0]) {
                swap(arrs, ++index, i);
            }
        }
        swap(arrs, left, index);
        quickSort(arrs, left, index - 1);
        quickSort(arrs, index + 1, right);
    }

    private void swap(int[][] arrs, int left, int right) {
        int[] tmp = arrs[left];
        arrs[left] = arrs[right];
        arrs[right] = tmp;
    }
}