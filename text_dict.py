#PY4E Dictionaries Chapter 9 Exercise 1+ (with custom file and string library)
import string

def text_dict():
    while True:
        fname = input("Enter file name: ")
        try:
            fhand = open(fname)
        except:
            print("Please keep your file in same folder and enter the file name with its extension")
            exit()

        words_dict = dict()
        for line in fhand:
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            words = line.split()
            for i in words:
                if not i in words_dict:
                    words_dict[i] = 1
                else:
                    words_dict[i] += 1

        input_words = input("Check the ocurrence of a word in the file: ")
        input_words = input_words.lower()

        try: 
            print(words_dict[input_words])
        except:
            print("Not found")

text_dict()