class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        # layer[结尾单词] = [ path1, path2 , path3 , ... ] ，其中每一个path都是以“结尾单词”结束的一组单词list，代表路径
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]
            # 保证 BFS，每一层好比声学传播的波前，所有的path都是最短路径
            wordList -= set(newlayer.keys())
            layer = newlayer

        return res