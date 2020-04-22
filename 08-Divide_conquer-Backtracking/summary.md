分治、回溯      
两者本质上属于递归       


### 1. 分治     
步骤：   
- （1）Divide：将problem分成多个sub-problems
- （2）Conquer：每个sub-problems得到sub-solutions
- （3）Merge：汇聚子问题的结果，得到final res        

```Python 
def divide_conquer(problem, param1, param2, ...):
    # rec terminator
    if problem is None:
        print res
        return
    
    # process data
    data = prepare_data(problem)
    sub_problems = split_problem(problem, data)

    # conquer sub_problems
    sub_res1 = self.divide_conquer(sub_problems[0], p1, ...)
    sub_res2 = self.divide_conquer(sub_problems[1], p2, ...)

    # process, generate final result
    res =  process_res(sub_res1, sub_res2)

```

### 2. 回溯
采用试错的思想，尝试分步去解决一个问题，    