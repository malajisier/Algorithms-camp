import java.util.concurrent.BlockingQueue;

public class BlockingQueueImpl {
    private final Object[] items;
    private int takeIdx;
    private int putIdx;
    private int count;
    
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition condition = lock.newCondition();

    public BlockingQueueImpl(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException();
        }
        items = new Object[capacity];
    }


    private void enqueue(Object obj) {
        items[putIdx] = obj;
        if (++putIdx == items.length)
            putIdx = 0;
        count++;
    }

    
    private Object dequeue() {
        Object obj = items[takeIdx];
        items[takeIdx] = null;

        if (++takeIdx == items.length)
            takeIdx = 0;
        
        count--;
        return obj;
    }

    public void put(Object obj) throws InterruptedException {
        // while (true) {
        //     synchronized (this) {
        //         if (count == items.length) {
        //             this.wait();
        //     }
        //     enqueue(obj);
        //     this.notifyAll();
        // }
        // }
        lock.lockInterruptibly();
        try {
            while (count == items.length) {
                condition.await();
            }
            enqueue(obj);
            condition.signalAll();
        } finally {
            lock.unlock();
        }
    }


    public Object take() throws InterruptedException {
        // while (true) {
        //     synchronized (this) {
        //         if (count == 0) {
        //             this.wait();
        //         }
        //     Object obj = dequeue();
        //     this.notifyAll();
        //     return obj;
        //     }
        // }
        lock.lockInterruptibly();
        try {
            while (count == 0) {
                condition.await();
            }
            Object obj = dequeue();
            condition.signalAll();
            return obj;
        } finally {
            lock.unlock();
        }
    }



    public static void main(String[] args) throws Exception{
        final BlockingQueue bq = new LinkedBlockingQueue<Integer>(2);
        final int threads = 2;
        final int times = 10;
        
        // 线程列表用于，等待所有线程完成执行
        List<Thread> threadList = new ArrayList<>(threads * 2);
        long startTime = System.currentTimeMillis();

        for (int i = 0; i < threads; i++) {
            final int offset = i * times;
            Thread producer = new Thread(() -> {
                try {
                    for (int j = 0; j < times; ++j) {
                        bq.put(new Integer(offset + j));
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });

            threadList.add(producer);
            producer.start();
        }


        for (int i = 0; i < threads; i++) {
            Thread consumer = new Thread(() -> {
                try {
                    for (int j = 0; j < times; ++j) {
                        Integer ele = (Integer)bq.take();
                        System.out.println(ele);
                    }
                } catch (Exception e) {
                    //TODO: handle exception
                    e.printStackTrace();
                }
            });
            
            threadList.add(consumer);
            consumer.start();
        }

        for (Thread thread : threadList) {
            thread.join();
        }

        long endTime = System.currentTimeMillis();
        System.out.println(String.format("总耗时： %.2fs", (endTime - startTime) / 1e3)); 
    }
}

