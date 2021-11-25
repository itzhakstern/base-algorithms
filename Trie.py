class Trie_Node:
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.word = False
        self.num_appears = 0


class Tries:
    def __init__(self):
        self.root = Trie_Node("")

    def insert(self, word):
        cur = self.root
        for item in word:
            if item not in cur.children:
                cur.children[item] = Trie_Node(item)
            cur = cur.children[item]
        cur.num_appears += 1
        cur.word = True

    def find(self, word):
        if not word:
            return True
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.word

    def is_word(self, word):
        cur = self.root
        for item in word:
            if item in cur.children:
                cur = cur.children[item]
            else:
                return False
        return cur.word

    def find_prefix(self, prefix):
        if not prefix:
            return self.root
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur

    def find_with_prefix_and_suffix(self, prefix, suffix, d):
        pre = self.find_prefix(prefix)
        if not pre:
            print("not find word with prefix: ", prefix)
            return None
        suf = []
        for c in pre.children:
            x = pre.children[c]
            self.__find_prefix_helper(pre.children[c], prefix+c, suf, suffix)
        return suf

    def __find_prefix_helper(self, node, word, suffix, s):
        cur = node
        w = ''
        for c in s:
            if c not in cur.children:
                return None
            cur = cur.children[c]
            w += c
        if cur.word:
            suffix.append(word+w)

    def print_words_with_prefix(self, prefix):
        if not prefix:
            return self.print_all()
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                print("not find words with this prefix")
                return
            cur = cur.children[c]
        return self.print_helper(cur, prefix)

    def num_appers(self, word):
        if not word:
            return 0
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                print("word not find")
                return
        return cur.num_appears

    def num_words_with_prefix(self, prefix):
        num = [0]
        if not prefix:
            self.num_words_helper(self.root, num)
            return num[0]
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                print("not find words with this prefix")
                return
            cur = cur.children[c]
        if cur.word:
            num[0] += 1
        self.__num_words_helper(cur,num)
        return num[0]

    def __num_words_helper(self, char, num):
        if not char.children:
            return 0
        for c in char.children:
            if char.children[c].word:
                num[0] = num[0]+1
            self.__num_words_helper(char.children[c], num)

    def print_all(self):
        self.__print_helper(self.root, "")

    def __print_helper(self, node, word):
        if not node.children:
            return
        for char in node.children:
            if not node.children[char].word:
                self.__print_helper(node.children[char], word + char)
            else:
                print(word + char)
                self.__print_helper(node.children[char], word + char)


words_lib = Tries()
words_lib.insert("aba")
words_lib.insert("caps")
words_lib.insert("abba")
words_lib.insert("apple")
words_lib.insert("axple")
words_lib.insert("caps")
words_lib.insert("cat")
words_lib.insert("appla")
words_lib.insert("cats")
words_lib.insert("caps")
words_lib.insert("ap")
# print(words_lib.find_with_prefix_and_suffix('a', "ple", 1))
# print(words_lib.num_words('ap'))
# print(words_lib.num_appers("caps"))

# words_lib.print_all()
# words_lib.print_words_with_prefix("ap")
# print(words_lib.find("cata"))