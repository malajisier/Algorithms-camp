### 思路：   
- 1.最大误区：不要人肉递归  
- 2.找到最近最简方法，将其拆解为可重复解决的问题，即重复子问题
- 3.数学归纳法思维     
   
**Python代码模板**     
```Python
def recursion(level, param1, param2):
    # 递归终止条件
    if level > max_level:
        process_result
        return 
    
    # 处理当前层逻辑
    process(level, data)

    # 下探到下一层
    self.recursion(level + 1, p1, ...)
```



  
### 递归的三点：   
- 1. 返回值
- 2. 调用单元做了什么
- 3. 终止条件

