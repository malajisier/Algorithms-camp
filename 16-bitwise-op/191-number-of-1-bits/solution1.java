// 循环和位移动，数字的每个位跟掩码1进行逻辑与运算，可以获得这个数字的最低位
/   / TC:O(1), 最坏32，  SC:O(1)

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int bits = 0;
        int mask = 1;

        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) {
                bits ++;
            }
            mask <<= 1;
        }

        return bits;
    }
}