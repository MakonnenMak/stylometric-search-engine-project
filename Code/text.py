import nltk
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
class TextProcess: 
    def preprocess(self,text):
        # Filtering random symbol from HTML parsing
        text = text.replace("&gt;","")
        # Tokenize sentence and make it lowercase
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens]
        #Punctuation filter
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        words = [word for word in stripped if word.isalpha()]
        #Remove stopwords
        #stop_words = set(stopwords.words('english'))
        #words = [w for w in words if not w in stop_words]
        return ' '.join(words)

    def pos_n_gram(self,text,n):
        tokens = word_tokenize(text)
        pos_tokens = nltk.pos_tag(tokens)
        n_grams =[]
        j = n
        for i in range(0,len(pos_tokens),n):
            filtered = pos_tokens[i:j]
            n_grams.append(filtered)
            j+=n

        output = [] 
        for n in n_grams:
            pos = ' '.join([y for x,y in n])
            output.append(pos)
        return output
   

#js = "And now for something completely"
#t =TextProcess()
#a = t.pos_n_gram(s,3)
#print(a)

#print(nltk.pos_tag(text))

