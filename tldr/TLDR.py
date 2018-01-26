from tldr.TFIDF import tfidf
import time


class TLDR:

    """Returns a summarized document
        @:param Needs document to be TextBlob objects and documents to be a list of textblob objects"""

    def __init__(self, document, documents):
        self.important_sentences = []
        self.indexes = []
        self.sentence_scores = {}
        self.doc = document
        self.docs = documents
        self.sentence_scores = {}
        self.sentences_by_relevance = {}

    def score_sentence(self, sentence_given):
        sentence_score = 0
        scores_dic = {word: tfidf(word, self.doc, self.docs) for word in self.doc.words}
        for word in scores_dic.keys():
            if word in sentence_given:
                sentence_score = sentence_score + scores_dic.get(word)
        return sentence_score

    def populate_scores(self):
        for sentence in self.doc.sentences:
            self.sentence_scores[sentence] = self.score_sentence(sentence)

    def sort_sentences(self):

        indexes = sorted(self.sentence_scores.values(), reverse=True)
        for index in indexes:
            for sentence, relevance in self.sentence_scores.items():
                if index == relevance:
                    self.important_sentences.append(sentence)

    def get_tldr_version(self, num_sentences):
        self.populate_scores()
        self.sort_sentences()
        summary = ''
        for i in range(0, len(self.important_sentences[:num_sentences])):
            summary = summary + " " + str(self.important_sentences[i])
        return summary


