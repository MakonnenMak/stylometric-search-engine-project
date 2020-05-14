import json
from text import *
from inverted_index import *
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
textProcessor = TextProcess()
with open('data/mid_subset.json') as json_file:
    for line in json_file:
        data = json.loads(line)
        if data["author"]!="[deleted]":
            author = data["author"]
            message = textProcessor.preprocess(data["body"])
            c = Comment(author,message)
            comments.append(c)

print("original search space")
print(len(comments))
inverted_index = InvertedIndex()
inverted_index.construct(comments)
inverted_index.search("flouride good holistic dentistry wackos and the weston a price foundation bad")


#y = TextPreProcess("&gt; Both are 100% efficient at converting electrical energy to heat.Nearly, but not quite. It's true that energy must be conserved, but it is not true to say that all the electrical energy is converted into heat. Other forms of energy are produced by both devices.") Inver 
#y.clean()
