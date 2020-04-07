from collections import defaultdict
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        n = len(beginWord)

        # defaultdict相较于dict，可以直接call一个不存在的key，如果key不存在直接创建，并根据默认值赋值value
        all_combination = defaultdict(list)
        # 相邻节点的所有组合方式
        for word in wordList:
            for i in range(n):
                all_combination[word[:i] + "*" + word[i + 1:]].append(word)

        dq = deque()
        dq.append((beginWord, 1))
        # 用bool字典标记被访问的，可以节省大量hashset操作
        visited = defaultdict(bool)
        visited[beginWord] = True

        while dq:
            cur_word, dist = dq.popleft()
            for i in range(n):
                cur_neighbors = all_combination[cur_word[:i] + "*" + cur_word[i + 1:]]
                for neighbor in cur_neighbors:
                    if neighbor == endWord:
                        return dist + 1
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        dq.append((neighbor, dist + 1))
        
        return 0
