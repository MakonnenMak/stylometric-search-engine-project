import json
from text import *
from inverted_index import *
import concurrent.futures
from top_posters import *
from statistics import mean

class Comment:
    def __init__(self,author,body):
        self.author = author
        self.body = body

comments = [] 
textProcessor = TextProcess()
with open('data/reddit_comments.json') as json_file:
    for line in json_file:
        data = json.loads(line)
        if data["author"]!="[deleted]":
            author = data["author"]
            message = textProcessor.preprocess(data["body"])
            c = Comment(author,message)
            comments.append(c)


top_posters_reddit = top_posters()
test_set = []
for i in comments:
    if i.author in top_posters_reddit.top:
        half = top_posters_reddit.top[i.author]//2
        j=0
        for comment in comments:
            if(j==half):
                break
            if comment.author==i.author:
                test_set.append(comment)
                comments.remove(comment)
                j+=1 


print("----------------------------------------------------")
print("original search space: ", len(comments))
inverted_index = InvertedIndex()
inverted_index.construct(comments)

global_success = 0

results = []
for test in test_set:
    success = 0
    ii_authors,length_of_results = inverted_index.search(test.body)
    if ii_authors:
        for author in ii_authors:
            if author==test.author:
                success+=1
                global_success+=1
    results.append(length_of_results)

print("----------------------------------------------------")
print("For a testing set of: ",len(test_set))
print("Overall successful hits: ", global_success)
print("----------------------------------------------------")
print("Average result size: ")
print("----------------------------------------------------")
print(mean(results))


