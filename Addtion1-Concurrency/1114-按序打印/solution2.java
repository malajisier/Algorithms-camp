/**
 * 通过 volatile设置一个全局标志位
 */

class Foo {
    private volatile int flag = 1;

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        flag = 2;
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (flag != 2);
        printSecond.run();
        flag = 3;
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (flag != 3);
        printThird.run();
    }
}