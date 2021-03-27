import java.util.LinkedList;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

class BoundedBlockingQueue {
    
    private LinkedList<Integer> queue = new LinkedList<>();
    private ReentrantLock lock = new ReentrantLock();
    private Condition empty = lock.newCondition();
    private Condition full = lock.newCondition();

    // 当前队列的元素个数
    private Integer size = 0;
    private Integer cap = null;

    public BoundedBlockingQueue(int capacity) {
        if (cap == null) {
            lock.lock();
            try {
                if (cap == null) {
                    cap = capacity;
                }
            } finally {
                lock.unlock();
            }
        }
    }

    public void enqueue(int element) throws InterruptedException {
        lock.lock();
        try {
            // 队列满的话，阻塞元素入队
            while (size >= cap) {
                full.await();
            }
            queue.offerFirst(element);
            size++;
            empty.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public int dequeue() throws InterruptedException {
        lock.lock();
        int res = -1;
        try {
            while (size == 0) {
                empty.await();
            }
            res = queue.pollFirst();
            size--;
            full.signalAll();
        } finally {
            lock.unlock();
        }
        return res;
    }

    public int size() {
        return size;
    }
}