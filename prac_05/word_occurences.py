
# Create occurrences dictionary
occurrences_dict = {}

# Set longest word length to 0
longest_word = 0

# Ask for the string to count the occurrences in
string = input("Enter a string to count the occurrence of words in: ")

# Split the string in to a list of words - Then sort alphabetically
string_wordlist = string.split()
string_wordlist.sort()

# Iterate through word list - Creating dictionary and finding longest word
for word in string_wordlist:
    word_length = len(word)
    if word_length > longest_word:
        longest_word = word_length
    occurrences_dict[word] = string_wordlist.count(word)
longest_word += 2

# Iterate through dictionary and print each pair with neat formatting
for item in occurrences_dict:
    word = "{} :".format(item)
    print("{:{}} {}".format(word, longest_word, occurrences_dict[item]))

