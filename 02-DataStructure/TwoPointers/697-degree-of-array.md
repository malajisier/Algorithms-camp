- 时间复杂度：O(n), 空间复杂度：O(n)   

```java
class Solution {
    public int findShortestSubArray(int[] nums) {
        // 遍历计算度
        int degree = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
            degree = Math.max(degree, map.get(num));
        }

        int l = 0, r = 0;
        int len = nums.length, res = len + 1;
        HashMap<Integer, Integer> count = new HashMap<>();
        // 固定右指针，收缩左指针
        while (r < len) {
            count.put(nums[r], count.getOrDefault(nums[r], 0) + 1);
            while (count.get(nums[r]) == degree) {
                res = Math.min(res, r - l + 1);
                count.put(nums[l], count.get(nums[l]) - 1);
                l++;
            }
            r++;
        }
        return res;
    }
}


// 写法二：抽取成函数  
class Solution {
    public int findShortestSubArray(int[] nums) {
        int l = 0, r = 0;
        int len = nums.length, res = len + 1;
        int degree = getDegree(nums);
        HashMap<Integer, Integer> map = new HashMap<>();

        while (r < len) {
            map.put(nums[r], map.getOrDefault(nums[r], 0) + 1);
            r++;

            // 收缩左指针
            // 因为求最短，右指针已+1，
            while (map.get(nums[r - 1]) == degree) {
                map.put(nums[l], map.get(nums[l]) - 1);
                res = Math.min(res, r - l);
                l++;
            }
        }
        return res;
    }

    public int getDegree(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int res = 0;
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
            res = Math.max(res, map.get(num));
        }
        return res;
    }
}

```