class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用字典层层嵌套，key为字符，value为下个字符的位置
        self.root = {}
        self.end_of_word = "#"


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            # setdefault，若字典包含key，返回其value，否则添加键并设置为默认值
            node = node.setdefault(letter, {})
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True