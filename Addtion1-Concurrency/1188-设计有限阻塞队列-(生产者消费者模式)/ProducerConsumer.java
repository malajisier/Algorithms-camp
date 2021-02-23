import java.util.concurrent.BlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class ProducerConsumer {
    // flag表示是否生产
    private volatile boolean falg = true;
    // aInt 表示产品
    private AtomicInteger aInt = new AtomicInteger();
    BlockingQueue<Object> queue = null;

    public ProducerConsumer(BlockingQueue<Object> queue) {
        this.queue = queue;
    }

    public void produce() throws Exception {
        String data = null;
        boolean retValue;
        while (flag) {
            data
        }
    }
}
