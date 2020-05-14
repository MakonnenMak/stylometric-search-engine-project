import json
from text import *
from inverted_index import *
import concurrent.futures

top_posters = {'cartooncorpse': 41, 'richardkulisz': 29, 'exobyte': 28, 'EggCoroner': 26, 'ayrnieu': 26, 'technosaur': 23, 'lespea': 22, 'drawkbox': 22, 'eadmund': 21, 'newton_dave': 20, 'boredzo': 19, 'smacfarl': 19, 'freshyill': 19, 'degustibus': 19, 'shorugoru': 19, 'joyork': 18, 'hiscity': 17, 'hiS_oWn': 17, 'nkktwotwozero': 17, 'bobcat': 17, 'look': 17, 'berlinbrown': 16, 'fishandchips': 16, 'degustistagecoach': 15, 'Formosus': 15, 'nosoupforyou': 14, 'khoury': 14, 'rukubites': 14, 'decaff': 14, 'NastyConde': 13, 'bluGill': 13, 'Shaper_pmp': 13, 'schizobullet': 12, 'jkerwin': 12, 'anachronic': 12, 'hopper': 12, 'Reg_Spyder': 11, 'Taladar': 11, 'chucker': 11, 'bruiser': 11, 'joelp': 11, 'sketerpot': 10, 'drosser': 10, 'chu': 10, 'carac': 10, 'chollida1': 10, 'toastspork': 10, 'lahuman8': 9, 'alaskamiller': 9, 'derefr': 9, 'Fountainhead': 9, 'dbenhur': 9, 'rancmeat': 9, 'rredit': 9, 'zach': 9, 'thehighercritic': 9, 'SpikeWolfwood': 9, 'joelthelion': 9, 'serpentjaguar': 9, 'electromagnetic': 9, 'MadMark': 8, 'slurpme': 8, 'muramasa': 8, 'souldrift': 8, 'cecilkorik': 8, 'GMPotato': 8, 'cgibbard': 8, 'jones77': 8, 'davidreiss666': 8, 'organic': 8, 'sbrown123': 8, 'jlowry': 8, 'pavel_lishin': 8, 'stubble': 8, 'isalpha': 8, 'mnemonicsloth': 8, 'jvance': 7, 'njharman': 7, 'mlkmnz': 7, 'NoMoreNicksLeft': 7, '42omle': 7, 'kingchiron': 7, 'emiller40': 7, 'vintermann': 7, 'radrik': 7, 'floatnsink': 7, 'rds260': 7, 'coldwarrior': 7, 'indigoshift': 7, 'breakneckridge': 7, 'lowdown': 7, 'xemu': 7, 'travisxt97': 6, 'tia-marie': 6, '9ner': 6, 'jerf': 6, 'mhd': 6, 'borg': 6, 'Entropy': 6, 'Whisper': 6}



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

test_set = []
for i in comments:
    if i.author in top_posters:
        half = top_posters[i.author]//2
        j=0
        for comment in comments:
            if(j==half):
                break
            if comment.author==i.author:
                test_set.append(comment)
                comments.remove(comment)
                j+=1 


print("original search space: ", len(comments))
inverted_index = InvertedIndex()
inverted_index.construct(comments)

success = 0
for test in test_set:
    ii_authors = inverted_index.search(test.body)
    if ii_authors:
        for author in ii_authors:
            if author==test.author:
                success+=1

print(len(test_set))
print(success)


