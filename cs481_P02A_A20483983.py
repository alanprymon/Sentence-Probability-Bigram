import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

nltk.download('brown')
nltk.download('reuters')
nltk.download('stopwords')



def frequencyDistribution(corpusIn) -> (list, list):
    #function completes part A1, A2
    #setup
    stopWordsCorpus = nltk.corpus.stopwords.words('english')
    words = corpusIn.words()
    #stripping stop words out of list
    words = [word for word in words if word.lower() not in stopWordsCorpus]
    #getting frequency distributions - part A1
    frequencyDistribution = nltk.FreqDist(word.lower() for word in words)
    frequenciesAndWords = dict()
    for word in words:
        frequenciesAndWords[word] = frequencyDistribution[word]
    frequenciesAndWords = list(frequenciesAndWords.items())
    #sorting the distribution
    frequenciesAndWords.sort(key=lambda a: a[1])
    frequenciesAndWords.reverse()
    #saving the labels and frequencies in seperate list in order
    labels, frequencies = map(list, zip(*frequenciesAndWords))
    #printing the top 10 most common 'words' - part A2
    for index in range(10):
        print(str(index + 1) + ' ' + labels[index])
    return labels, frequencies

def plotFreqRank() -> None:

    return

if __name__ == '__main__':
    corpusBrown = nltk.corpus.brown
    corpusReuters = nltk.corpus.reuters
    '''stopWordsCorpus = nltk.corpus.stopwords.words('english')
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
        print(str(index + 1) + ' ' + labels[index])'''
    labels, frequencies = frequencyDistribution(corpusBrown)

    labels2 = labels[:1000]
    frequencies2 = frequencies[:1000]
    fig, ax = plt.subplots()
    xs = range(len(labels))
    labels2 = range(len(labels))

    def format_fn(tick_val, tick_pos):
        if int(tick_val) in xs:
            return labels2[int(tick_val)]
        else:
            return ''

    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(xs, frequencies)
    ax.set_title('Token frequency counts in corpus ranked')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlabel('log(Rank)')
    plt.ylabel('log(Frequency count)')
    plt.show()

    totalWordsBrown = 0
    for i in frequencies:
        totalWordsBrown += i
    techAmount = 0
    for i in range(len(labels)):
        if labels[i] == 'work':
            techAmount = frequencies[i]
            break
    print(techAmount/totalWordsBrown)


    print('debug')
