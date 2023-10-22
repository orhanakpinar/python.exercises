#Python for Everybody Chapter 5 Exercises
def addsup_calc():
    total = list()
    while True:
        inp = input("Please enter a number to add up or enter 'done' to complete your action or enter 'quit' to exit:")
        try:
            inp = inp.replace(",", ".")
        except:
            inp = inp       
        if inp == "done":
            try:
                print("Sum is:", sum(total), "Average is:", sum(total)/len(total), "Total number of input:", len(total))
                print("Max value is:", max(total), "Min value is:", min(total))
                total.clear()
            except:
                print("No result for 0 entry")
        elif inp == "quit":
            quit()
        else: 
            try:
                calc = float(inp)
                print(calc)
                total.append(calc)
            except:
                print("Please enter a value")          
                    
addsup_calc()
    
    
 
        
