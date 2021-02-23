#### 1. while循环法改进版

`while`循环跑满CPU，会影响GIL线程上下文切换的判定，可能是导致超时的重要原因之一，`time.sleep`会把CPU交还给GIL，可以让GIL及时切换线程

```python
class Foo:
    def __init__(self):
        self.t = 0
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
        self.t = 1
        
    def second(self, printSecond: 'Callable[[], None]') -> None:
		while self.t != 1:
            sleep(1e-9)
        printSecond()
        self.t = 2
        
    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.t != 2:
            sleep(1e-9)
        printThird()
```



#### 2. Lock 锁对象

```python
import threading as t

class Foo:
    # 类初始化的时候不能包含有参数，所以需要acquire进行阻塞，调用其他函数的时按顺序release释放
    def __init__(self):
        self.l1 = t.Lock()
        self.l1.acquire()
        self.l2 = t.Lock()
        self.l2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.l2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```



#### 

#### 3. 信号量法

```python
import threading

class Foo:
    def __init__(self):
        self.sem1 = threading.Semaphore(0)
        self.sem2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sem1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.sem1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.sem2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.sem2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```



#### 4. Event事件对象法

```python
import threading
# 用wait方法作为阻塞，用set来释放线程，默认类赋值就是阻塞的
class Foo:
    def __init__(self):
        self.e1 = threading.Event()
        self.e2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:        
        printFirst()
        self.e1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.e1.wait()
        printSecond()
        self.e2.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e2.wait()
        printThird()
```



#### 5. Barrier 栅栏对象法

定义了`parties = 2`个等待线程，调用完了`parties`个`wait`就会释放线程

```python
import threading

class Foo:
    def __init__(self):
        self.b1 = threading.Barrier(2)
        self.b2 = threading.Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:        
        printFirst()
        self.b1.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()
```



#### 6. Queue 阻塞队列

```python
import queue
# 使用阻塞队列，队列为空时，get方法会自动阻塞，直到put方法使之非空才会释放线程
class Foo:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:        
        printFirst()
        self.q1.put(0)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()
```



#### 7. Condition 条件对象法

```python
import threading

class Foo:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        # with 是常配合Condition 使用的语法糖
        with self.c:
            # wait_for阻塞每个函数，直到self.t 为目标值时才释放线程
            self.c.wait_for(lambda: val == self.t)   # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()

```

