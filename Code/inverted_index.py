
class InvertedIndex:
    def __init__(self):
        self.comments = dict()
        self.inverted_index = dict()

    def construct(self,comment_data):
        i = 0 
        for c in comment_data:
            self.comments[i]=c
             

        


