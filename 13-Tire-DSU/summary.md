## 1.Trie树/字典树      
取自英文Retrieval中的一部分，也称为检索树、单词查找树、键树。典型应用是用于统计和排序大量的字符串，常被搜索引擎系统用于文本词频统计      
核心思想：空间换时间，**利用字符串的公共前缀来降低查询时间的开销，来提高效率**。      
优点：最大限度减少无谓的字符串比较，查询效率高于哈希表       
https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode/      

### （1）字典树的基本性质     
- 节点本身不存完整单词      
- 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串      
- 每个节点的所有子节点路径代表的字符都不相同         


## 2.并查集    
（1）适用场景：组团、配对问题        
（2）基本操作：
- makeSet(s): 建立一个新的并查集，包含s个元素
- unionSet(x, y): 如果x、y所在集合不相交，把元素x、y所在集合合并，否则不合并
- find(x): 找到元素x所在集合代表，该操作可用来判断两个元素是否位于同一集合     
   
（3）典型题目        
岛屿数量、朋友圈       

（4）代码模板        
- Java模板
```Java
class UnionFind {
    private int count = 0;
    private int[] parent;
    
    // 初始化并查集
    public UnionFind(int n) {
        count = n;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // 查找p所在集合和所在集合的领头元素(parent[i]=i)
    public int find(int p) {
        while (p != parent[p]) {
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }

    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;
        // 不相等的话，把俩集合合并
        parent[rootP] = rootQ;
        // 合并后独立的集合减少一个
        count--;
    }
}       
```     

- Python模板      
```Python
def init(p):
    p = [i for i in range(n)]  

def union(self, p, i, j):
    p1 = self.parent(p, i) 
    p2 = self.parent(p, j)
    # 找到各自的领头元素后，合并
    p[p1] = p2

def parent(self, p, i):
    root = i
    # 直接返回root也可以
    while p[root] != root:
        root = p[root]
    
    # 优化：路径压缩，把可以指向root的元素，指向root，缩短下次元素查找领头元素的时间（O(1)）
    while p[i] != i:
        x = i
        i = p[i]
        p[x] = root
    
    return root
```



    