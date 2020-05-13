from bs4 import BeautifulSoup
class TextPreProcess(self):
    def __init__(self,text):
        self.text = text
    
    def clean(self):
        soup = BeautifulSoup(self.text, 'html.parser')
        print(soup)


