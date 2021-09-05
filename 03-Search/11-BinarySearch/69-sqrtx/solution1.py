# 注意边界问题
class Solution:
    def mySqrt(self, x):
        l = 0
        # 对于一个非负数n，它的平方根不会大于（n/2+1）
        r = (x / 2) + 1
        
        while l <= r:
            mid = l + (r- l) // 2
            num = mid * mid

            if num == x:
                return int(mid)
            elif num < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return int(r)