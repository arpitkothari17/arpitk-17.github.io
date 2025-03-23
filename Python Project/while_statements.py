#%% Q1 - FLOW 3.b
laptop = input("Enter the brand of laptop required: ").lower().strip()
while laptop not in ["apple","acer","toshiba","hp","imb","lenovo"]:
    print("Sorry we don't provide this brand.")
    laptop = input("Place order from another brand: ").lower().strip()
    
print("Perfect! We'll the order for", laptop.title(), "laptop")
    
#%% Q2
name = input("Enter your name: ").strip().title()
while name[0] != "A":
    print("Sorry, enter a name starting with 'A'")
    name = input("Enter another name: ").strip().title()    

print("That's a great name", name)

#%% Q3
num = int(input("Enter a number: "))
while num < 10:
    print("No, we need a number greater than 10")
    num = int(input("Enter another number: "))    
    
print("Perfect! Thanks")

#%% Q4 
num1 = float(input("Enter a number: "))
attempt = 1 
while num1 < 10:
    print("No, we need a number greater than 10")
    num1 = float(input("Enter another number: "))
    attempt += 1 
    if attempt > 5:
        #print("Sorry you only had 6 attempts.")
        break
    
#print("Thanks for your number")
#%% Q5 (OPTIONAL)

num2 = float(input("Enter a number: "))
num_high = num2
while num2 >= 0:
    if num2 > num_high:
        num_high = num2
    num2 = float(input("Enter another number: "))

print("The biggest number is", num_high)

#%% Q6 - TAMARA AROSEMENA (-if)
sale = float(input("Enter today's sale: "))
if sale >= 25:
    print("Great job", sale, "is higher than average.")
else:
    print("You need to do better, you sale is lower than average.")
#%% Q6 - TAMARA AROSEMENA (-while)
sale1 = float(input("Enter today's sales: "))
while sale1 <= 25:
    print("You need to do better!")
    sale1 = float(input("Do you want to enter a new sale record: "))
    
print("Great job.")
#%% Q6 - MOUATH ALDEHEISH
num3 = ""
num_sum = sum(num3)
while num3 != 9:
    num3 = float(input("Enter another number: "))
    print("The sum so far is", num_sum)
    
print("The total sum is,", num_sum)
#%%
