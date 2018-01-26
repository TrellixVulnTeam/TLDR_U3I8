import math


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def docs_containing(word, bloblist):
    """Checks how many times a word is in """
    num_times = 0
    for blob in bloblist:
        if word in blob.words:
            num_times = num_times + 1
    if num_times == 0:
        return 1  # There must be at least one occurrence. Fail safe.
    return num_times


def idf(word, bloblist):
    return math.log(len(bloblist)) / (1 + docs_containing(word, bloblist))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
