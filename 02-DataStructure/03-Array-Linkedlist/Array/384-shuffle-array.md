#### 洗牌算法     
过程：  
- 每次迭代中，生成一个范围在 **当前下标到数组末尾元素下标** 之间的随机整数，下标对应元素互换  
- PS: 当前元素是可以和它本身互相交换的        

复杂度：   
- TC: O(n), 生成随机序列，交换两个元素这两种操作都是常数时间复杂度的, SC:O(n)   


```java
class Solution {
    private int[] array;
    private int[] original;
    Random random = new Random();

    public Solution(int[] nums) {
        array = nums;
        original = nums.clone();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        array = original;
        original = original.clone();
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        for (int i = 0; i < array.length; i++) {
            int pos = random.nextInt(array.length - i) + i;
            swap(i, pos);
        }
        return array;
    }

    private void swap(int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

```