import nltk
import matplotlib.pyplot as plt

nltk.download('brown')
nltk.download('reuters')
nltk.download('stopwords')

if __name__ == '__main__':
    corpusBrown = nltk.corpus.brown
    corpusReuters = nltk.corpus.reuters
    stopWordsCorpus = nltk.corpus.stopwords.words('english')
    wordsBrown = corpusBrown.words()
    wordsBrown = [w for w in wordsBrown if w.lower() not in stopWordsCorpus]
    frequencyDistribution = nltk.FreqDist(word.lower() for word in wordsBrown)
    frequenciesAndWords = dict()
    for word in wordsBrown:
        frequenciesAndWords[word] = frequencyDistribution[word]
    frequenciesAndWords = list(frequenciesAndWords.items())
    frequenciesAndWords.sort(key=lambda a: a[1])
    frequenciesAndWords.reverse()
    labels, frequencies = map(list, zip(*frequenciesAndWords))
    for index in range(10):
        print(str(index) + ' ' + labels[index])
    print('debug')
