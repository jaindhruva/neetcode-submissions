class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None]*26


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root 
        for c in word:
            if node.children[ord(c)-ord('a')] is None:
                node.children[ord(c)-ord('a')] = TrieNode()
            node = node.children[ord(c)-ord('a')]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root 
        return self.searchNode(word, node)
    
    def searchNode(self, word: str, node: TrieNode) -> bool:
        for i,c in enumerate(word):
            if c == '.':
                for n in node.children:
                    if n is None:
                        continue
                    if self.searchNode(word[i+1:], n):
                        return True
                return False
            if node.children[ord(c)-ord('a')] is None :
                return False
            node = node.children[ord(c)-ord('a')]
        return node.isWord