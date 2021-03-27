import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

/**
 * 信号量实现：
 * 
 */

class ZeroEvenOdd {
    private int n;
    private Semaphore semZero = new Semaphore(1); // 初始化时已有一个许可，先执行打印零
    private Semaphore semEven = new Semaphore(0);
    private Semaphore semOdd = new Semaphore(0);
    
    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            semZero.acquire();
            printNumber.accept(0);

            if (i % 2 == 0) {
                // 执行打印奇数方法
                semOdd.release();
            } else {
                semEven.release();
            }
        }
        
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            semEven.acquire();
            printNumber.acquire(i);
            semZero.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            semOdd.acquire();
            printNumber.accept(i);
            semZero.release();
        }
    }
}