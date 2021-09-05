### 法一：重写比较器   
- 挑出日志中的 字母和数字类别，分别放到两个list 
- 字母list 使用自定义比较器排序，数字list顺序保持不变    
  

```java
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        int n = logs.length;
        if (n == 1) return logs;

        List<String> alpha = new ArrayList<>();
        List<String> nums = new ArrayList<>();

        for (String log : logs) {
            int pos = log.indexOf(" ") + 1;
            if ('0' <= log.charAt(pos) && log.charAt(pos) <= '9') {
                nums.add(log);
            } else {
                alpha.add(log);
            }
        }

        alpha.sort(new Comparator<String>() {
            @Override
            public int compare(String str1, String str2) {
                int pos1 = str1.indexOf(" ");
                int pos2 = str2.indexOf(" ");
                // 分别取出 标识符和内容
                String identifier1 = str1.substring(0, pos1);
                String content1 = str1.substring(pos1 + 1);
                String identifier2 = str2.substring(0, pos2);
                String content2 = str2.substring(pos2 + 1);

                int cmp = content1.compareTo(content2);
                // 内容相同时，标识符也按字典序排列
                if (cmp == 0) {
                    return identifier1.compareTo(identifier2);
                } else {
                    return cmp;
                }
            }
        });

        String[] res = new String[n];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (i < alpha.size()) {
                res[idx++] = alpha.get(i);
            } else {
                // 先输出的字母list，i 需减去其偏移量
                res[idx++] = nums.get(i - alpha.size());
            }
        }
        return res;
    }
}
```