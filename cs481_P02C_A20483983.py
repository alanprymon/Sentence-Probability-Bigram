import nltk

nltk.download('brown')
nltk.download('stopwords')

def nextBestThree(first: str, corpusInput: list) -> ((str, float), (str, float), (str, float)):
    bigrams = nltk.bigrams(corpusInput)
    choices = dict()
    for x in corpusInput:
        choices[x] = 0
    total_count_first = 0
    for x in bigrams:
        if x[0] == first:
            total_count_first += 1
            choices[x[1]] = choices[x[1]] + 1
    choices = list(choices.items())
    choices.sort(key=lambda a: a[1], reverse=True)
    return [(choices[0][0], choices[0][1]/total_count_first), (choices[1][0], choices[1][1]/total_count_first), (choices[2][0], choices[2][1]/total_count_first)]

if __name__ == '__main__':
    words = nltk.corpus.brown.words()
    stopWordsCorpus = nltk.corpus.stopwords.words('english')
    # stripping stop words out of list and lowercasing at the same time
    words = [word.lower() for word in words if word.lower() not in stopWordsCorpus]
    good = False
    inWord = input("Enter a word: ")
    while not good:
        if inWord in words:
            good = True
        else:
            option = input("Not a valid word choose an option:\n  a.  ask again\n  b.  QUIT")
            match option:
                case 'b':
                    exit(0)
                case _:
                    #since an input of anything other than allowed defaults to the first one as written in assignment
                    inWord = input("Enter a word: ")
    sentence = inWord
    while True:
        topThree = nextBestThree(inWord, words)
        option = input(40*'-'+"\n"+sentence+"\nWhich word should follow:"+
            "\n1) "+topThree[0][0]+" P("+inWord+" "+topThree[0][0]+") = "+str(topThree[0][1])+
            "\n2) "+topThree[1][0]+" P("+inWord+" "+topThree[1][0]+") = "+str(topThree[1][1])+
            "\n3) "+topThree[2][0]+" P("+inWord+" "+topThree[2][0]+") = "+str(topThree[2][1])+
            "\n4) QUIT\n")
        match option:
            case '2':
                inWord = topThree[1][0]
                sentence += ' ' + inWord
            case '3':
                inWord = topThree[2][0]
                sentence += ' ' + inWord
            case '4':
                print("Final sentence: \""+sentence+"\"")
                exit()
            case _:
                inWord = topThree[0][0]
                sentence += ' ' + inWord