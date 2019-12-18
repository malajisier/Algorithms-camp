// 维护一个单调栈，直接利用C++中的stack数据结构

class MinStack {
public:
    stack<int> stk;
    stack<int> min_stack;
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        stk.push(x);
        if(min_stack.empty() || x <= min_stack.top()) {
            min_stack.push(x);
        }
    }
    
    void pop() {
        if(stk.top() == min_stack.top())  
            min_stack.pop();
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};