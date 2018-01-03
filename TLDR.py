from textblob import TextBlob
from TFIDF import tfidf


class TLDR:
    important_sentences = []
    indexes = []
    """Returns a summarized document
        @:param Needs document and documents to be TextBlob objects"""

    def __init__(self, document, documents):
        self.doc = document
        self.docs = documents

    def sentence_score(self, sentence):
        sentence_score = 0
        for word in sentence.words:
            sentence_score = sentence_score + TLDR.word_score(word)

    def word_score(self, word):
        score = tfidf(word, self.doc, self.docs)
        return score

    def score_sentences(self):
        for sentence in self.doc.sentences:
            self.indexes.append(TLDR.sentence_score(sentence))
# Make a dictionary with the score and corresponding sentence. Make another dic with the indexes sorted (highest is
# higher). You then run a for loop which loops through the original dictionary and appends the value if the key matches
#  the item of the sorted list. The sorted list will only have scores.
