import nltk

nltk.download('punkt_tab')
nltk.download('brown')

def bigramTableConstructor(corpusInput) -> (list, list, list):
    #lots of looping, huge 2D list, and really slow to build so I decided to not use this and instead use bigramProb for each bigram
    bigrams = nltk.bigrams(corpusInput.words())
    first_word_axis = []
    second_word_axis = []
    bigram_table = []
    total_count = 0
    for x in bigrams:
        current_bigram = x
        first_word = current_bigram[0].lower()
        second_word = current_bigram[1].lower()
        if first_word not in first_word_axis:
            first_word_axis.append(first_word)
            bigram_table.append([])
            for _ in second_word_axis:
                bigram_table[-1].append(0)
        if second_word not in second_word_axis:
            second_word_axis.append(second_word)
            for row in bigram_table:
                row.append(0)
        x = first_word_axis.index(first_word)
        y = second_word_axis.index(second_word)
        bigram_table[x][y] += 1
        total_count += 1 #also this var is wrong for what I want to use it for
    #and this for loop below is wrong because of above wrong var
    for x in range(len(first_word_axis)):
        for y in range(len(second_word_axis)):
            bigram_table[x][y] = bigram_table[x][y] / total_count
    return first_word_axis, second_word_axis, bigram_table

def bigramProb(bigramInput: (str, str), corpusInput) -> float:
    bigrams = nltk.bigrams(corpusInput.words())
    total_count_first = 0
    total_count_exact = 0
    for x in bigrams:
        if bigramInput[0] == x[0].lower():
            total_count_first += 1
            if bigramInput[1] == x[1].lower():
                total_count_exact += 1
    return total_count_exact / total_count_first

if __name__ == '__main__':
    sentence = input("Input a sentence: ")
    print("Original sentence: \"" + sentence + "\"")
    sentence = sentence.lower()
    sentence0 = sentence
    sentence = nltk.word_tokenize(sentence) #Using this instead of split to handle punctuation, etc easier
    sentence = [grams for grams in nltk.bigrams(sentence)]
    sentenceProb = []
    print("Each bigram probability:\n" + "(<$>, " + sentence[0][0] + ") -> P(" + sentence[0][0] + ", <$>) = 0.25")
    for x in sentence:
        sentenceProb.append(bigramProb(x, nltk.corpus.brown))
        print("(" + x[0] + ", " + x[1] + ") -> P(" + x[1] + ", " + x[0] + ") = " + str(sentenceProb[-1]))
    print("(" + sentence[len(sentence)-1][1] + ", <$/>) -> P(<$/>, " + sentence[len(sentence)-1][1] + ") = 0.25")
    finalProbability = 0.25 * 0.25
    for x in sentenceProb:
        finalProbability = finalProbability * x
    print("P(" + sentence0 + ") = " + str(finalProbability))
