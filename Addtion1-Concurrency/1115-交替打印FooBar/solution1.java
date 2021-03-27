/**
 * 信号量实现
 */

class FooBar {
    private int n;
    private Semaphore semFoo = new Semaphore(1);
    private Semaphore semBar = new Semaphore(0);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            semFoo.acquire();
        	printFoo.run();
            semBar.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            semBar.acquire();
        	printBar.run();
            semFoo.release();
        }
    }
}