#Python for Everybody, Chapter6 Exercise 3

def letter_count():  
    while True:    
        inp_sent = input("Please enter some sentence or word to count the letter occurences:")
        inp_word = input("Please enter the letter for searching through your entry:")
        let_count = 0
        inp_sent = inp_sent.lower()
        inp_word = inp_word.lower()
        if len(inp_word) > 1:
            print("Please enter a single letter at a time.")
        elif len(inp_word) == 0  or len(inp_sent) == 0:
            print("Please enter a letter.")
        else:
            let_count = 0
            for lt in inp_sent:
                if lt == inp_word:
                    let_count = let_count + 1
            print(let_count)
        
letter_count()




