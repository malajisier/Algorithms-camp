class Solution {
    public String reverseOnlyLetters(String S) {
        Stack<Character> letters = new Stack();

        for (char c : S.toCharArray()) {
            if (Character.isLetter(c))
                letters.push(c);
        }

        StringBuilder res = new StringBuilder();
        for (char c : S.toCharArray()) {
            if (Character.isLetter(c))
                res.append(letters.pop());
            else
                res.append(c);
        }

        return res.toString();
        
    }
}