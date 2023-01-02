# Importing the required libraries
# import nltk 
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize, sent_tokenize

# # Function to extract the proper nouns 

# def ProperNounExtractor(text):
    
#     print('PROPER NOUNS EXTRACTED :')
    
#     sentences = nltk.sent_tokenize(text)
#     for sentence in sentences:
#         words = nltk.word_tokenize(sentence)
#         words = [word for word in words if word not in set(stopwords.words('english'))]
#         tagged = nltk.pos_tag(words)
#         print(tagged)

# text =  "A room with blue walls and a white sink."

# # Calling the ProperNounExtractor function to extract all the proper nouns from the given text. 
# ProperNounExtractor(text)

# import spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("A room with blue walls and a white sink.")
# for chunk in doc.noun_chunks:
#     print(chunk.text)

from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import Tree
 
nlp = StanfordCoreNLP('stanford-corenlp-4.5.1')
 
s = 'A room with blue walls and a white sink'
def get_noun_phrases(nlp,text):
    tree=Tree.fromstring(nlp.parse(text.lower()))
    noun_phrases=[]
    queue=[(tree,0,len(tree.leaves()))]
    while len(queue)!=0:
        accumulate=0
        tmp=queue[0][0]
        start=queue[0][1]
        length=queue[0][2]
        queue.pop(0)
        for subtree in tmp:
            if not isinstance(subtree,str):
                queue.append((subtree,start+accumulate,len(subtree.leaves())))
                if subtree.label()=='NP' and len(tree.leaves())!=len(subtree.leaves()) and len(subtree.leaves())>1:
                    noun_phrases.append((' '.join(subtree.leaves()),start+accumulate,len(subtree.leaves())))
                accumulate+=len(subtree.leaves())
    return noun_phrases 

 
print(get_noun_phrases(nlp,s))
nlp.close()#释放，否则后端服务器将消耗大量内存

