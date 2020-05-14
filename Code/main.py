import json
from tree import Tree
from text import TextPreProcess
import concurrent.futures

'''
1) Read comments in preprocess the comments []
2) Create post object with author and processed comment []
3) Add comments via style to II []
4) Test 500 authors to see how many we get in the top k []
'''

class Comment:
    def __init__(self,author,body):
        self.author = author
        self.body = body

comments = [] 
with open('data/reddit_comments.json') as json_file:
    for line in json_file:
        data = json.loads(line)
        if data["author"]!="[deleted]":
            author = data["author"]
            message = TextPreProcess(data["body"])
            c = Comment(author,message.clean())
            comments.append(c)



with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    trees = list(executor.map(lambda c: Tree(c.body), comments))
    pickle.dump(trees, output, pickle.HIGHEST_PROTOCOL)
    del trees
print('done')


#y = TextPreProcess("&gt; Both are 100% efficient at converting electrical energy to heat.Nearly, but not quite. It's true that energy must be conserved, but it is not true to say that all the electrical energy is converted into heat. Other forms of energy are produced by both devices.")
#y.clean()
