需要求最大值，可以用大根堆   

### 法一：堆/优先队列  
- TC:O(nlogn)，堆排的复杂度； SC:O(n),堆需要的空间
```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        int n = nums.length;
        /** 
         * 优先队列存放的是二元组(num,index) :
         * 大顶堆: 元素大小不同按元素大小排列，元素大小相同按下标进行排列
         */
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] pair1, int[] pair2) {
                return pair1[0] != pair2[0] ? pair2[0] - pair1[0] : pair2[1] - pair1[1];
            }
        });

        // 初始化堆，堆顶就是最大元素
        for (int i = 0; i < k; i++) {
            pq.offer(new int[]{nums[i], i});
        }
        int[] res = new int[n - k + 1]; 
        res[0] = pq.peek()[0];

        for (int i = k; i < n; i++) {
            pq.offer(new int[]{nums[i], i});
            while (pq.peek()[1] <= i - k) {
                pq.poll();
            }
            res[i - k + 1] = pq.peek()[0];
        }
        
        return res;
    }
}
```   

### 法二：deque/单调队列
- 队列元素 非严格递减，队首 是当前窗口最大值
- TC:O(n)，每个元素或下标 入队一次，最多出队一次；SC:O(k)

```java
// 写法一：双指针指向滑动窗口头尾，存值
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0 || nums == null) return new int[0];
        Deque<Integer> deque = new LinkedList<>();
        int n = nums.length;
        int[] res = new int[n - k + 1];

        for (int j = 0, i = 1 - k; j < n; i++, j++) {
            // 如果队首 是左边界的前一个，说明已不在窗口里，删除
            if (i > 0 && deque.peekFirst() == nums[i - 1]) {
                deque.removeFirst();
            }
            while (!deque.isEmpty() && deque.peekLast() < nums[j]) {
                deque.removeLast();
            }
            deque.offer(nums[j]);
            if (i >= 0) {
                res[i] = deque.peekFirst();
            }
        }
        return res;
    }


```