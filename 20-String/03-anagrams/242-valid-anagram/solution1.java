class Solution {
    public boolean isAnagram(String s, String t) {
        // 长度必须相同
        if (s.length() != t.length()) return false;

        int[] alpha = new int[26];
        // 统计s 中每个字母的出现次数，使用t 减少计数器每个字母的出现次数
        for (int i = 0; i < s.length(); i++) {
            alpha[s.charAt(i) - 'a'] ++;
            alpha[t.charAt(i) - 'a'] --;
        }
        
        // 两种判断方式：
        // 若为有效异位词，计数后每个字母的出现次数为0
        for (int i = 0; i < 26; i++) {
            if (alpha[i] != 0) return false;
        }

        // for (int count : alpha) {
        //     if (count != 0) return false;
        // }

        return true;
    }
}