// 双指针法，维护一个指针j 倒序遍历字符串，前面的指针i 遇到字母时就使用j

class Solution {
    public String reverseOnlyLetters(String S) {

        StringBuilder res = new StringBuilder();
        int j = S.length() - 1;

        for (int i = 0; i< S.length(); ++i) {
            if (Character.isLetter(S.charAt(i))) {
                while (!Character.isLetter(S.charAt(j))) 
                    j--;
                res.append(S.charAt(j--));
            } else {
                res.append(S.charAt(i));
            }
        }

        return res.toString();
    }
}