/**
 * java中有内置的链表，实现较简单一些
 */

class MyHashSet {
    private Bucket[] bucket;
    private int keyRange;

    /** Initialize your data structure here. */
    public MyHashSet() {
        this.keyRange = 769;
        this.bucket = new Bucket[this.keyRange];
        for (int i = 0; i < this.keyRange; ++i) {
            this.bucket[i] = new Bucket();
        }
    }

    protected int _hash(int key) {
        return (key % this.keyRange);
    }
    
    public void add(int key) {
        int bucketIndex = this._hash(key);
        this.bucket[bucketIndex].insert(key);
    }
    
    public void remove(int key) {
        int bucketIndex = this._hash(key);
        this.bucket[bucketIndex].delete(key);
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        int bucketIndex = this._hash(key);
        return this.bucket[bucketIndex].exists(key);
    }
}

class Bucket {
    private LinkedList<Integer> container;

    public Bucket() {
        container = new LinkedList<Integer>();
    }
    
    public boolean exists(Integer key) {
        int index = this.container.indexOf(key);
        return (index != -1);
    }

    public void insert(Integer key) {
        int index = this.container.indexOf(key);
        if (index == -1) {
            this.container.addFirst(key);
        }
    }

    public void delete(Integer key) {
        this.container.remove(key);
    }
}