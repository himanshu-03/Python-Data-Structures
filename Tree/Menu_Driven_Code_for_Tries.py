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

# Dynamic input for words
while True:
    user_input = raw_input("Enter a word (or 'q' to quit): ")  # Use raw_input for Python 2.x
    if user_input == 'q':
        break
    trie.insert(user_input)

# Dynamic input for searching
while True:
    user_input = raw_input("Enter a word to search (or 'q' to quit): ")  # Use raw_input for Python 2.x
    if user_input == 'q':
        break
    if trie.search(user_input):
        print("'{0}' is found in the trie.".format(user_input))
    else:
        print("'{0}' is not found in the trie.".format(user_input))


