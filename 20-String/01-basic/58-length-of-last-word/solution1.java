class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        // end 负责过滤掉尾部的空格，指向最后一个单词的最后一个字符
        while (end >= 0 && s.charAt(end) == ' ') end--;
        if (end < 0)  return 0;

        // start 负责计算最后一个单词的长度，从最后一个字符开始遇到空格为止
        int start = end;
        while (start >= 0 && s.charAt(start) != ' ') start--;
        
        return end - start;
    }
}