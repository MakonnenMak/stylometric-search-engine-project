import nltk
from nltk import word_tokenize
class TextPreProcess:
    def __init__(self,text):
        self.text = text
    
    def clean(self):
        self.text = self.text.replace("&gt;","")
        return self.text


