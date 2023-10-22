#python for everybody - chapter 3 the grade calculator exercises

inp = input("Please enter a grade between 1 and 0:")

#if someone uses comma for tenths
try: 
    inp = inp.replace(",", ".")
except:
    inp = inp
    
    
try:
    grade = float(inp) 
except:
    print("Input value is not a number\nPlease enter a valid number")
    quit()


if grade >= 0 and grade <= 1:
    if grade < 0.6 and grade >=0:
        print("Score is F")
    elif grade < 0.7:
        print("Score is D")
    elif grade < 0.8 :
        print("Score is C")
    elif  grade < 0.9  :
        print("Score is B")
    elif grade <= 1:
        print("Score is A")

else:
    print("Please enter a valid number")

 
#quitting after showing the answer

