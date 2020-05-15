from text import *
N = 3
textProcessor = TextProcess()
class InvertedIndex:
    def __init__(self):
        self.comments = dict()
        self.inverted_index = dict()

    def construct(self,comment_data):
        i = 0 
        for c in comment_data:
            self.comments[i]=c
            n_gram = textProcessor.pos_n_gram(c.body,N)
            for n in n_gram:
                if n not in self.inverted_index:
                    self.inverted_index[n]=set()
                self.inverted_index[n].add(i)
            i+=1

    def search(self,query):
        query = textProcessor.preprocess(query)
        n_gram = textProcessor.pos_n_gram(query,N)
        matching_comments = set()
        for n in n_gram:
            if n in self.inverted_index:
                matching_comments.update(self.inverted_index[n])
        
        if len(matching_comments)==0:
            return [],0

        matching_authors = set()
        for comment in matching_comments:
            matching_authors.add(self.comments[comment].author)
        
        return matching_authors,len(matching_authors)


    
        
             

        


