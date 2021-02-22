class MyQueue {
    private int front;
    private Stack<Integer> s1;
    private Stack<Integer> s2;

    public MyQueue() {
        front = 0;
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    // TC:O(N),  SC:O(N)
    public void push(int x) {
        if (s1.empty()) 
            front = x;
        while (!s1.isEmpty()) {
            s2.push(s1.pop());
        }
        s2.push(x);
        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }
    }
    
    public int pop() {
        int pop = s1.pop();
        if (!s1.isEmpty()) 
            front = s1.peek();
        return pop;
    }
    
    public int peek() {
        return front;
    }
    
    public boolean empty() {
        return s1.isEmpty();
    }
}
