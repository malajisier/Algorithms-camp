/**
 * https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/java-dan-diao-shuang-xiang-lian-biao-hua-tu-xiang-/
 * 
 * 使用queue双端队列：存储的是索引，严格保证队列头部是最大值
 */


class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 1) {
            return new int[0];
        }

        int idx = 0;
        int[] res = new int[nums.length - k + 1];
        LinkedList<Integer> queue = new LinkedList<>();

        for (int i = 0; i< nums.length; i++) {
            while (!queue.isEmpty() && nums[queue.peekLast()] <= nums[i]) {
                queue.pollLast();
            }

            // 正常添加索引
            queue.addLast(i);
            // 窗口已略过队首元素，删除
            if (queue.peekFirst() == (i - k)) {
                queue.pollFirst();
            }

            // 每形成 k大小的窗口时，收集最大值
            if (i >= (k - 1)) {
                res[idx++] = nums[queue.peekFirst()];
            }
        }
        return res;
    }
}