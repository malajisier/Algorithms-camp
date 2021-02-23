/**
 * 使用 condition
 */

class FooBar {
    private int n;
    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            lock.lock();
        	try {
                printFoo.run();
                condition.await();
            } finally {
                lock.unlock();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
        	lock.lock();
            try {
                printBar.run();
                condition.signal();
            } finally {
                lock.unlock();
            }
        }
    }
}