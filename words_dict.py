#PY4E Dictionaries Chapter 9 Exercise 1

fhand = open('words.txt')

words_list = list()
for line in fhand:
    words = line.split()
    words_list = words_list + words
    
words_dict = {}
for i in words_list:
    words_dict[i] = None

input_words = input("Check if a word is in the dictionary:")
print(input_words in words_dict)

