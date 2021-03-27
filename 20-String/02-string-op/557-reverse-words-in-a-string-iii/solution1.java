 // 使用内置函数  
 // TC:O(N), SC:O(N)

 class Solution {
    public String reverseWords(String s) {
        String words[] = s.split(" ");
        StringBuilder res = new StringBuilder();
        for (String str : words) {
            res.append(new StringBuffer(str).reverse().toString() + " ");
        }

        return res.toString().trim();
    }
}


