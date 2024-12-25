def replace_word(sentence, word1, word2):
    return sentence.replace(word1, word2)

sentence = input("Enter a sentence: ")
word1 = input("Enter the word to replace: ")
word2 = input("Enter the replacement word: ")
print(replace_word(sentence, word1, word2))