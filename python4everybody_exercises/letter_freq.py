#PY4E Chapter 10 Exercise 3, Frequency of a letter in a text file
#Visit https://wikipedia.org/wiki/Letter_frequencies for comparing results

import string

def letter_freq():
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
        
        letters_dict = dict()
        for x in words_dict:
            for z in x:
                if z not in letters_dict:
                    letters_dict[z] = 1 * words_dict[x]
                else:
                    letters_dict[z] = letters_dict[z] + words_dict[x]
        #print(letters_dict)
        sum_letters = 0  
        for keys in letters_dict:
            sum_letters = sum_letters + letters_dict[keys]

        
        
        input_letters = input("Check the frequence of a letter in the file: ")
        input_letters = input_letters.lower()

        try:
            freq_percent = 100 * (letters_dict[input_letters]/sum_letters)     
            freq_perc_str = str(round(freq_percent, 2))
            print(freq_perc_str + "%")
        except:
            print("Bad data")

        
        

letter_freq()

#couldn't make it work with pdf encoding