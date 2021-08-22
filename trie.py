import config

class TrieNode():

    def __init__(self):
        self.children = {}
        self.last = []


class Trie():
    __instance = None

    @staticmethod
    def getInstance():
        if not Trie.__instance:
            Trie()
        return Trie.__instance

    def __init__(self):
        if Trie.__instance:
            raise Exception("Trie is singleton class,"
                            " Instead of initial new Instance you"
                            " can use the getInstance() method.")
        Trie.__instance = self
        self.root = TrieNode()

    def insert(self, string, id_of_sen):
        node = self.root
        for a in list(string):
            config.index -= 1
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
            if config.index == 0:
                break
        node.last.append(id_of_sen)

    def search(self, key):
        index_array=[]
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            self.extend_sub_tree(node,index_array)
        return index_array


    def extend_sub_tree(self,node,sol,word=''):
        sol.extend(node.last)
        for a, n in node.children.items():
            self.extend_sub_tree(n,sol, word + a)


    def print_trie(self,node=None,word=''):
        if not node:
            node=self.root
        else:
            print(word+':')
            for item in node.last:
                print(item,end=" ")
            print('\n')

        for a, n in node.children.items():
            self.print_trie(n, word + a)

    def search_with_added(self, key, index=1):
        index_array = []
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a) and index:
                index -= 1
                continue
            elif not node.children.get(a):
                found = False
                break
            node = node.children[a]
        if found and node:
            self.extend_sub_tree(node, index_array)
        return index_array

    def search_with_clear(self, key, index=1):
        sol = []
        self.search_with_clear_rec(key, sol, index)
        return sol

    def search_with_clear_rec(self, key, index_array, index, index_of_a=0, node=None):
        if not node:
            node = self.root
        found = True
        for a in list(key[index_of_a:]):
            if not node.children.get(a) and index:
                found = False
                index -= 1
                for k, v in node.children.items():
                    # print(k, v)
                    self.search_with_clear_rec(key, index_array, index, index_of_a, v)
                continue
            elif not node.children.get(a):
                found = False
                break
            node = node.children[a]
            index_of_a += 1
        if found and node:
            self.extend_sub_tree(node, index_array)