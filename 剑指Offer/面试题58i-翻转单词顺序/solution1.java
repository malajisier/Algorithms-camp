// 双指针法，从后往前搜索
class Solution {
    public String reverseWords(String s) {
        // 去除首位空格
        s = s.trim();
        int j = s.length() - 1, i = j;

        StringBuilder res = new StringBuilder();
        while (i >= 0) {
            // j 指向尾部字符，索引i 从后向前搜索第一个空格
            while (i >= 0 && s.charAt(i) != ' ') i--;
            // 遇到空格，就把遍历完的单词加入结果
            res.append(s.substring(i + 1, j + 1) + " ");
            while (i >= 0 && s.charAt(i) == ' ') i--;
            // 索引j 指向倒数第二个单词的末尾
            j = i;
        }

        return res.toString().trim();
    }
}