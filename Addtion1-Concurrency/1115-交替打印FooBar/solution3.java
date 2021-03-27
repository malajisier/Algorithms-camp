/** 有时会超时，不推荐
 * 设置全局标志位
 */
class FooBar {
    private int n;
    private volatile boolean finish = false;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            while (finish) {
                // 线程让步可以让，当前线程继续执行，不可靠
                Thread.yield();
            }            
        	printFoo.run();
            finish = true;
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            while (!finish) {
                Thread.yield();
            }
        	printBar.run();
            finish = false;
        }
    }
}