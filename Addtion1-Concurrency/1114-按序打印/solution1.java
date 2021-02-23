/**
 * 通过 信号量
 */

class Foo {
    private Semaphore spa, spb;
    public Foo() {
        spa = new Semaphore(0);
        spb = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        spa.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        spa.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        spb.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        spb.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}