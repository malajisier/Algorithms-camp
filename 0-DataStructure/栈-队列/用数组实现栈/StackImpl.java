public class StackImpl {
    public static class ArrayStack {
        private Integer[] arr;
        private Integer index;

        public ArrayStack(int size) {
            if (size < 0) {
                throw new IllegalArgumentException("The init size is less than 0");
            }
            arr = new Integer[size];
            index = 0; 
        }

        // 取栈顶元素
        public Integer peek() {
            if (index == 0) {
                return null;
            }
            return arr[index - 1];
        }

        // 压栈
        public void push(int num) {
            if (index == arr.length) {
                throw new ArrayIndexOutOfBoundsException("The stack is full.");
            }
            arr[index++] = num;
        }

        // 出栈
        public Integer pop() {
            if (index == 0) {
                throw new ArrayIndexOutOfBoundsException("The stack is empty.");
            }
            return arr[--index];
        }
    }
}