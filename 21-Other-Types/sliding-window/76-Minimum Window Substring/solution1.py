# py版的使用字典实现

import numpy as np
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        start = 0
        min_len = np.inf

        window = {}
        needs = dict((i, t.count(i)) for i in t)

        match = 0

        while r < len(s):
            s1 = s[r]
            if s1 in needs.keys():
                window[s1] = window.get(s1, 0) + 1
                if window[s1] == needs[s1]:
                    match += 1
            r += 1
        
            while match == len(needs):
                if r - l < min_len:
                    start = l
                    min_len = r - l
                
                s2 = s[l]
                if s2 in needs.keys():
                    window[s2] -= 1
                    if window[s2] < needs[s2]:
                        match -= 1
                l += 1
        
        return '' if min_len == np.inf else s[start : start + min_len]