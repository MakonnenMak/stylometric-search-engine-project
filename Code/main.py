import json
from tree import Tree
from text import TextPreProcess

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
        else:
            counter+=1

#x = Tree("Hello John, how are you?")
#x.generate_tree()
#x.print_tree()

#y = TextPreProcess("&gt; Both are 100% efficient at converting electrical energy to heat.Nearly, but not quite. It's true that energy must be conserved, but it is not true to say that all the electrical energy is converted into heat. Other forms of energy are produced by both devices.")
#y.clean()
