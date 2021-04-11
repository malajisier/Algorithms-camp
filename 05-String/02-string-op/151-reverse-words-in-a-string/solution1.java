class Solution {
    public String reverseWords(String s) {
        // trim：去掉字符串头尾空格
        String[] words = s.trim().split(" +");
        Collections.reverse(Arrays.asList(words));
        return String.join(" ", words);
    }
}