# Function to replace a word in a sentence
def replace_word(sentence, word1, word2):
    # Replace all occurrences of word1 with word2 in the sentence
    return sentence.replace(word1, word2)

# Ask the user to input a sentence
sentence = input("Enter a sentence: ")

# Ask the user to input the word they want to replace
word1 = input("Enter the word to replace: ")

# Ask the user to input the replacement word
word2 = input("Enter the replacement word: ")

# Call the replace_word function and print the result
print(replace_word(sentence, word1, word2))
