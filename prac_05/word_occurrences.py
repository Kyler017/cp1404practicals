def main():
    sentence = input("please enter sentence: ")
    words = {}
    number_of_words = 0
    for word in sentence.split():
        word = word.lower().strip()
        number_of_words = max(number_of_words,len(words))
        words[word] = words.get(word,0) + 1
    words_of_counts = list(words.items())
    words_of_counts.sort()
    for word,count in words_of_counts:
        print(f"{word:{number_of_words}}:{count}")
main()