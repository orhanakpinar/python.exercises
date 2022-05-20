total = list()

def addsup_calc():
    while True:
        inp = input("Please enter a number to add up or enter 'done' to complete your action:")
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
        else: 
            try:
                calc = float(inp)
                print(calc)
                total.append(calc)
            except:
                print("Please enter a value")          
                    
while True:
    addsup_calc()
    
    
 
        
