
inp = input("Please enter a grade between 1 and 0:")


try: 
    inp = inp.replace(",", ".")
except:
    inp = inp
try:
    grade = float(inp) 
except:
    print("Please enter a valid number")



while grade >= 0 and grade <= 1:
    if grade < 0.6 and grade >=0:
        print("Score is F")
        break
    elif grade < 0.7:
        print("Score is D")
        break
    elif grade < 0.8 :
        print("Score is C")
        break
    elif  grade < 0.9  :
        print("Score is B")
        break
    elif grade <= 1:
        print("Score is A")
        break
    else:
        print("enter a valid number")
else:
    print("Please enter a valid number")

 


