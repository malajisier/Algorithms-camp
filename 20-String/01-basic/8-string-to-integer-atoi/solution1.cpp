class Solution {
public:
    int myAtoi(string str) {
        int res = 0, i = 0, flag = 1;

        while (str[i] == ' ') i++;
        if (str[i] == '-') flag = -1;
        if (str[i] == '+' | str[i] == '-') i++;

        while (i < str.size() && isdigit(str[i])) {
            int digit = str[i] - '0';
            
            // 判断整数是否溢出
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && digit > 7)) {
                return flag > 0 ? INT_MAX : INT_MIN;
            }
            res = res * 10 + digit;
            i++;
        }
        return flag > 0 ? res : -res;
    }
};