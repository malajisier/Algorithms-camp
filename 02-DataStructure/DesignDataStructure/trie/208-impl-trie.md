






```java
// 法一：
class Trie {
    class TrieNode {
        TrieNode[] next = new TrieNode[26]; // 字母映射表
        boolean end; // 当前节点 是否是一个str的结束
    }

    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode cur = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (cur.next[idx] == null) {
                cur.next[idx] = new TrieNode();
            }
            cur = cur.next[idx];
        }
        cur.end = true;
    }
    
    public boolean search(String word) {
        TrieNode cur = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (cur.next[idx] == null) {
                return false;
            }
            cur = cur.next[idx];
        }
        // PS：不能直接返回TRUE，
        // word可能是个前缀，也能正常退出循环，但是end标志位为空
        return cur.end;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        for (int i = 0; i < prefix.length(); i++) {
            int idx = prefix.charAt(i) - 'a';
            if (cur.next[idx] == null) {
                return false;
            }
            cur = cur.next[idx];
        }
        return true;
    }
}
```   


```java
// 法二：无需定义node，
class Trie {
    private Trie[] children;
    private boolean isEnd;

    public Trie() {
        children = new Trie[26];
        isEnd = false;
    }
    
    public void insert(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new Trie();
            }
            node = node.children[idx];
        }
        node.isEnd = true; 
    }
    
    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private Trie searchPrefix(String prefix) {
        Trie node = this;
        for (int i = 0; i < prefix.length(); i++) {
            int idx = prefix.charAt(i) - 'a';
            if (node.children[idx] == null) {
                return null;
            }
            node = node.children[idx];
        }
        return node;
    }
}
```


```python 
# py实现
class Trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word: str) -> None:
        tree = self.lookup
        for ch in word:
            if ch not in tree:
                tree[ch] = {}
            tree = tree[ch]
        tree["#"] = "#";

    def search(self, word: str) -> bool:
        tree = self.lookup
        for ch in word:
            if ch not in tree:
                return False
            tree = tree[ch]
        return True if "#" in tree else False

    def startsWith(self, prefix: str) -> bool:
        tree = self.lookup
        for ch in prefix:
            if ch not in tree:
                return False
            tree = tree[ch]
        return True
```