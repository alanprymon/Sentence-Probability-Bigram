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
    print("top 10 words:")
    for index in range(10):
        print(str(index + 1) + ': ' + labels[index])
    print(6*'-')
    return labels, frequencies

def plotFreqRank(labels: list, frequencies: list, whichcorpus: str) -> None:
    #function completes part A3
    #setup of size of graph and what values to look/plot
    labels2 = labels[:1000]
    frequencies2 = frequencies[:1000]
    fig, ax = plt.subplots()
    xs = range(len(labels2))
    labels2 = range(len(labels2))

    def format_fn(tick_val, tick_pos):
        if int(tick_val) in xs:
            return labels2[int(tick_val)]
        else:
            return ''

    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    #put values into graph
    ax.plot(xs, frequencies2)
    #setup of title, axis titles, and scale to log
    ax.set_title('Token frequency counts in ' + whichcorpus + ' corpus ranked [first 1000 tokens]')
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.xlabel('log(Rank)')
    plt.ylabel('log(Frequency count)')
    plt.show()
    return

def unigramExample(labels: list, frequencies: list, testword: str) -> None:
    #getting total number of words in corpus by adding all frequencies up
    totalWords = 0
    for i in frequencies:
        totalWords += i
    #adding amount of the word in the corpus by finding it then using that index getting the frequency
    wordAmount = 0
    for i in range(len(labels)):
        if labels[i].lower() == testword:
            wordAmount += frequencies[i]
    #printing everything out
    print("total count of words in corpus: " + str(totalWords))
    print("total count of \"" + testword + "\" in corpus: " + str(wordAmount))
    print("unigram occurrence probability for \"" + testword + "\": " + str(wordAmount / totalWords))
    return

if __name__ == '__main__':
    corpusBrown = nltk.corpus.brown
    corpusReuters = nltk.corpus.reuters
    #doing everything for the brown corpus
    print(10*"-"+"For the Brown corpus"+10*"-")
    labels1, frequencies1 = frequencyDistribution(corpusBrown)
    plotFreqRank(labels1, frequencies1, "Brown")
    unigramExample(labels1, frequencies1, "remunerate")
    unigramExample(labels1, frequencies1, "work")
    #doing everything for the reuters corpus
    print(10 * "-" + "For the reuters corpus" + 10 * "-")
    labels2, frequencies2 = frequencyDistribution(corpusReuters)
    plotFreqRank(labels2, frequencies2, "Reuters")
    unigramExample(labels2, frequencies2, "remunerate")
    unigramExample(labels2, frequencies2, "work")