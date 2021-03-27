/**
 * 使用CountDownLatch实现
 * 每当一个任务线程执行完毕，就将计数器减 1 countdownlatch.countDown()
 * 当计数器的值变为 0 时，在CountDownLatch上 await() 的线程就会被唤醒
 */

class ZeroEvenOdd {
    private int n;
    private CountDownLatch cd1 = new CountDownLatch(0);
    private CountDownLatch cd2 = new CountDownLatch(1);
    private CountDownLatch cd3 = new CountDownLatch(1);    

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            cd1.await();
            printNumber.accept(0);
            cd1 = new CountDownLatch(1);
            if (i % 2 == 0) {
                cd3.countDown();
            } else {
                cd2.countDown();
            }
        }
    }   

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            cd2.await();
            printNumber.accept(i);
            cd2 = new CountDownLatch(1);
            cd1.countDown();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            cd3.await();
            printNumber.accept(i);
            cd3 = new CountDownLatch(1);
            cd1.countDown();
        }
    }
}