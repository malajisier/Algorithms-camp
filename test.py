
        if not digits: return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
            print(ls1)
        return ls1

if __name__ == "__main__":
    digits = '23'
    print(Solution().letterCombinations(digits))