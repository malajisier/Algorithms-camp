import java.util.LinkedList;
import java.util.concurrent.Semaphore;

class BoundedBlockingQueue {
    private Semaphore consumerSem;
    private Semaphore producerSem;
    private int capacity;
    private LinkedList<Integer> queue = new LinkedList<Integer>();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        consumerSem = new Semaphore(0);
        producerSem = new Semaphore(capacity);
    }

    public void enqueue(int element) throws InterruptedException {
        producerSem.acquire();
        queue.add(element);
        consumerSem.release();
    }

    public int dequeue() throws InterruptedException {
        consumerSem.acquire();
        int popValue = queue.removeFirst();
        producerSem.release();
        return popValue;
    }

    public int size() {
        return queue.size();
    }
}