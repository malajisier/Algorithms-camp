public class QueueImpl {
    public static class ArrayQueue {
        private Integer[] arr;
        private Integer capacity;
        private Integer start;
        private Integer end;

        public ArrayQueue(int size) {
            arr = new Integer[size];
            capacity = 0;
            start = 0;
            end = 0;
        }

        // 返回队首元素
        public Integer peek() {
            return arr[start];
        }

        
        /**
         * 出入队首先判断是否越界，必须走的第一步
         */

        // 入队
        public void push(int num) {
            // end超过数组大小时，无法入队
            if (end < arr.length - 1) {
                end++;
            } else {
                throw new ArrayIndexOutOfBoundsException("The Queue is full.");
            }
            arr[end] = num;
            capacity++;         
        }

        // 出队
        public Integer pull() {
            if (start < arr.length - 1) {
                start++;
            } else {
                throw new ArrayIndexOutOfBoundsException("The Queue is full.");
            }
            int pull_idx = start;
            capacity--;
            return arr[pull_idx];
        }
    }
}