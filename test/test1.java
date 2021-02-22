public class test1 {
    public static Integer valueOf(int i ) {
        if (i >= IntegerCache.low && i <= IntegerCache.high) 
            return 
    }
}


public class A {
    private int x;
    private static int y;

    public static void main(String[] main) {
        A a = new A();
        int x = a.x;
        int y = A.y;
        System.out.println(x + y);
    }
}