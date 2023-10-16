"""
# Menu Driven Code for Tries also known as a prefix tree, a tree-like data structure 
used for efficient retrieval of a key in a dataset of strings. 
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
words = ["apple", "banana", "orange", "app", "ban", "or"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # True
print(trie.search("appl"))  # False
print(trie.starts_with("app"))  # True
print(trie.search("ban"))  # True
print(trie.search("banana"))  # True
print(trie.search("band"))  # False
