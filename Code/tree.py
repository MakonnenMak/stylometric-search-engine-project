'''
Stylometric Search Engine
'''

# Imports

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = './StanfordNLP/stanford-parser-full-2018-10-17'
os.environ['STANFORD_MODELS'] = './StanfordNLP/stanford-parser-full-2018-10-17'

class Tree:

    def __init__(self,value):
        self.value = value
        self.tree = None

    def generate_tree(self):
        # StanfordParser() function will become depracated 
        sp = stanford.StanfordParser()
        tree = [t for t in sp.parse(self.value.split())]
        self.tree = tree
        return

    def print_tree(self):
        if self.tree:
            print(self.tree[0])
        else:
            print("Tree Not Initialized")



