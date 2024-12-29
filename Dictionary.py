from nltk.corpus import wordnet
# Download WordNet if not already downloaded

# import nltk
# nltk.download('wordnet')
while True:
    word = input("Enter a word: ")
    if word == "":
        print("Exiting program...")
        break
    else:
        print(f"Meanings for {word}:")
        # Get synonyms
        synonyms = wordnet.synsets(word)


        # Print definitions
    for synonym in synonyms:
        print("======================")
        print(f"Definition: {synonym.definition()}")
        print("\n")
        print(f"Example: {synonym.examples()}")
        print("\n")
        print(f"Synonyms: {synonym.lemmas()}")
        print("======================")
        print("\n")
        continue