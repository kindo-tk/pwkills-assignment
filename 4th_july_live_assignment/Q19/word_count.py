from collections import Counter
import string

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Sort the word counts dictionary by key (alphabetically)
    sorted_word_counts = dict(sorted(word_counts.items()))
    
    # Display the results
    print("Word occurrences in alphabetical order:\n")
    for word, count in sorted_word_counts.items():
        print(f"{word}: {count}")

# Provide the path to the text file
file_path = 'paragraph.txt'
count_words(file_path)
