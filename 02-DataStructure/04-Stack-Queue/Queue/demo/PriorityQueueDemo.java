import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;

public class PriorityQueueDemo {
    public static void main(String[] args) {
        Queue<Integer> intPriorityQueue = new PriorityQueue<>(1);
        Random random = new Random();

        for (int i = 0; i < 10; i++) {
            intPriorityQueue.add(Integer.valueOf(random.nextInt(100)));
        }
        for (int i = 0; i < 10; i++) {
            Integer in = intPriorityQueue.poll();
            System.out.println("processing integer: " + in);
        }

        // 使用随机数 生成随机用户对象
        Queue<Customer> customerPriorityQueue = new PriorityQueue<>(10, idComparator);
        addDataToQueue(customerPriorityQueue);
        pollDataFromQueue(customerPriorityQueue);

    }

    public static Comparator idComparator = new Comparator<Customer>() {
        @Override
        public int compare(Customer c1, Customer c2) {
            return (int)(c1.getId() - c2.getId());
        }
    };

    private static void addDataToQueue(Queue<Customer> customerPriorityQueue) {
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            int id = random.nextInt(100);
            customerPriorityQueue.add(new Customer(id, "pow" + id));
        }
    }

    private static void pollDataFromQueue(Queue<Customer> customerPriorityQueue) {
        while (true) {
            Customer customer = customerPriorityQueue.poll();
            if (customer == null) break;
            System.out.println("processing customer with ID= " + customer.getId());
        }
    }
}
