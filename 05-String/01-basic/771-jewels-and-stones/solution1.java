// TC:O(n+m), SC:O(n)

class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jset = new HashSet();
        for (char j: J.toCharArray()) {
            jset.add(j);
        }

        int count = 0;
        for (char s: S.toCharArray()) {
            if (jset.contains(s)) {
                count++;
            }
        }

        return count;
    }
}