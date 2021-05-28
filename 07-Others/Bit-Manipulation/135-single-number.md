- 尝试用哈希表   
- 空间复杂度O(n)，不满足O(1)要求   

```java

```


### 法一：异或    
- 异或运算XOR，特点：
  - 一个数和 0 做 XOR 运算等于本身：a⊕0 = a
  - 一个数和其本身做 XOR 运算等于 0：a⊕a = 0
  - XOR 运算满足交换律和结合律，  a⊕b⊕a = (a⊕a)⊕b = 0⊕b = b  

- 将所有数字按照顺序做抑或运算，最后剩下的结果即为唯一的数字  
- 时间复杂度：O(n)，空间复杂度：O(1)    


```java
class Solution {
    public int singleNumber(int[] nums) {
        // 两个相同的数异或为0，最后异或到 那个不重复的数字，结果就是它
        int single = 0;
        for (int num :nums) {
            single ^= num;
        }
        return single;
    }
}
```