# 支付5元：得到5元
# 支付10元：必须找回一张5元
# 支付20元：必须找回15元
#   - 优先找一张10元和5元
#   - 否则找三张5元，最后无法找回返回false

class Solution(object):
    def lemonadeChange(self, bills):
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            
            elif bill == 10:
                ten += 1

            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            
        return True