import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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
        print(str(index + 1) + ' ' + labels[index])

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



    print('debug')
