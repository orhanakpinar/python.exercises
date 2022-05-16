#python for everybody exercise 4, making grade_calc a function

while True: #To loop the program

    x = input("Please enter a grade between 1 and 0:")
    #If the user enters a comma for decimals
    try: 
        x = x.replace(",", ".")
    except:
        x = x 
    #If user enters a string input   
    try:
        x = float(x) 
    except:
        print("Input value is not a number")
        continue     

    #Wrapping grade_calc here    
    def grade_func(x):
        while x >= 0 and x <= 1:
            if x < 0.6 and x >=0:
                return("Score is F")
                break
            elif x < 0.7:
                return("Score is D")
                break
            elif x < 0.8 :
                return("Score is C")
                break
            elif  x < 0.9  :
                return("Score is B")
                break
            elif x <= 1:
                return("Score is A")
                break

    if x >= 0 and x <= 1:
        print(grade_func(x))
    else:
        print("Please enter a valid number")

#this function repeats itself