```python
# python解法
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按每个小区间的头 升序排序
        intervals.sort(key = lambda x : x[0])

        merge = []
        for interval in intervals:
            # 上一区间的末尾 小于 当前区间的头，说明无重叠            
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                # 对比两个区间末尾大小，选大的合并
                merge[-1][1] = max(merge[-1][1], interval[1])
        
        return merge
```





```java
class Solution {
    public int[][] merge(int[][] intervals) {
        // 简洁写法
        Arrays.sort(intervals, (v1, v2) -> v1[0] - v2[0]);
        
        // 重写comparator
        // Arrays.sort(intervals, new Comparator<int[]>() {
        //    public int compare(int[] interval1, int[] interval2) {
        //        return interval1[0] - interval2[0];
        //    }
        //});
        
        int[][] res = new int[intervals.length][2];
        int idx = -1;

        for (int[] interval : intervals) {
            if (idx == -1 || interval[0] > res[idx][1]) {
                res[++idx] = interval;
            } else {
                res[idx][1] =  Math.max(res[idx][1], interval[1]);
            }
        }

        return Arrays.copyOf(res, idx + 1);
    }
}
```

