class Node:
    def __init__(self):
        self.children = {}      # contain children nodes
        self.isEnd = False      # is it closing node

class WordDictionary:
    def __init__(self):
        self.root = Node()  # init root node . Empty

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = Node()    # add to children new key value
            currentNode = currentNode.children[char]      # change pointer to new node . Just created
        currentNode.isEnd = True

    def search(self, word: str) -> bool:
        currentLevelNodes = [self.root]         # start from ROOT elem
        # for each letter in word
        for c in word:
            nextLevelNodes = []
            if c == '.':
                for node in currentLevelNodes:
                    nextLevelNodes.extend(node.children.values())
            else:
                for node in currentLevelNodes:
                    if c in node.children:
                        nextLevelNodes.append(node.children[c])

            if not nextLevelNodes:
                return False
            currentLevelNodes = nextLevelNodes

        for node in currentLevelNodes:
            if node.isEnd:
                return True

        return False


# string = 'axb'
# pattern = '[a-z]x[a-z]'
# print(re.search(pattern, string).group(0))

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))            # return False
print(wordDictionary.search("bad"))             # return True
print(wordDictionary.search(".ad"))      # return True
print(wordDictionary.search("b.."))      # return True
#
#
# ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
# [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]


wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print(wordDictionary.search("."))
print(wordDictionary.search("a"))
print(wordDictionary.search("aa"))
print(wordDictionary.search("a"))
print(wordDictionary.search(".a"))
print(wordDictionary.search("a."))