try: # try inside the code try if the code throws error then print the except code
    num=int(input("Enter Number: "))
    def print_table(n):
        for i in range(1,11):
            print(f"{n}x{i}={n*i}")
    print_table(num)
except:
    print("Wrong input chq this Again")
    
try: # try inside the code try if the code throws error then print the except code
    num=int(input("Enter Number: "))
    a=['ram','sham','honey','money']
    print(a[num])

    
except:
    print("Wrong input chq this Again")