flag = 0 
while flag <= 10:
    print(flag)
    flag += 1 # > flag = flag + 1 
    
#%% Flow.4 (not right)
import random
rand = random.randint(1,20)    

rand_user = float(input("Guess a number: "))

while rand_user != rand:
    print("Sorry, the value was", rand)
    rand_user = float(input("\nSorry, guess again: "))

print("Congratulation, you guessed it right.")
        
#%% Flow.3
ran1 = random.randint(1,20)
ran2 = random.randint(1,10)

print("The addition of the numbers is:", ran1+ran2)
print("The floor division of the numbers is:", ran1//ran2)

ran1_u = float(input("Guess the 1st value:"))
ran2_u = float(input("Guess the 2nd value:"))

while ran1_u != ran1 or ran2_u != ran2:
    print("\nNope, try again")
    ran1_u = float(input("Guess the 1st value:"))
    ran2_u = float(input("Guess the 2nd value:"))

print("Congrats, you got them right")

#%% FLOW3.B
laptop = input("Enter the laptop you need: ").title()

while laptop not in ["Hp", "Apple", "Lenovo", "Acer", "Toshiba"]:
    print("Not possible, maybe in the future")
    
print("We'll place the order and notify you")
   
#%% (Optional ex-6)

air_info1 = "Sun, 03/11, 01:20:15 JED-BOM"
air_info2 = "Sat, 02/11, 15:25:15 Mad-Jed"
air_info3 = "Sun, 03/11, 17:05:15 BOM-UDP"

flight = int(input("Enter the hours and minutes: "))
             
f1 = air_info1[21:]
f2 = air_info2[21:]
f3 = air_info3[21:]

t1 = float(air_info1[12:17])
t2 = float(air_info2[12:17])
t3 = float(air_info3[12:17])

#%% Session 6 
mys = range(0,110,10)
for i in mys:
    print(i)
    
a = range(0,101,10)
for b in a:
    if b < 50:
        continue
    print(b)

    
a = range(0,101,10)
for b in a:
    if b > 50:
        break
    print(b)
    
#%% 
name = ['arpit', 'ishan', 'alexia', 'barra', 'anibal', 'maragrita', 'zarifa']

#name_len = len(name)

for n in name:
    if len(n) >= 6:
        print(n.title(), "- The best")
    else:
        print(n.title(),"- The second best")
#%%
name = ['arpit', 'ishan', 'alexia', 'barra', 'anibal', 'maragrita', 'zarifa']

for a in name:
    if a[0] == 'a':
        print(a.title())
#%% Flow.5
import webbrowser
news = ["https://www.bbc.com","https://www.euronews.com/","http://www.abyznewslinks.com/europ.htm"]

for n in news:
    news1 = webbrowser.open(url=n)
    print(news1)
#%% FLOW.5 (Corrected)
sites = ["https://www.bbc.com","https://www.euronews.com/","http://www.abyznewslinks.com/europ.htm"]
for url in sites:
    webbrowser.open(url)
    
#%% DS4
age = [23, 50, 60, 60, 69, 67, 56, 56, -4, 10, 9]
for a in age: 
    if a < 0:
        print("Warning: Negative Values found")
        break

age.sort()
if age[0]< 0:
    print("Warning: Negative Values found")
    
#%%
# Show total rev for top 3 clients 
rev = [200,500,40,0,20,-10,50,20]
rev.sort()
rev.reverse()
print(sum(rev[0:3]))
#%% DS5
email = ["p.m@canalytic.es", "a.k@gmail.com", "ma@ie.edu", "br@voadaphone.com"]

for e in email:
    c = [(e.split("@")[-1])]
    for n in c:
        print(n.split(".")[0].title())
    
lane = "record street of the art"
lane.split("street")
#%% DS.10

ID = [1,4,5,6,78,67,4,5,4,6,32,12]
len(ID)

ID1 = set(ID)
len(ID1)

li = ['Juan', 'Fransisco', 'Norman']
if "Juan" in li:
    li.remove("Juan")
print(li)
del (li[1])
print(li)

grades = ["Arpit - 10", "Pablo - 7", "Mark - 4"]

# Print students who failed the exam 
for fail in grades:
    if float(fail[-2:]) <= 5:
        print("Sorry, you failed", fail)
    else:
        print("Congratulations, you passsed", fail)
    
# Try to guess my birthday
    # 3 attempts at max
month = input("Guess my birthday month: ").title().strip()
attempt = 1 
while month != "December":
    print("\nSorry, wrong guess")
    month = input("Guess again: ").title().strip()
    attempt = attempt + 1
    if attempt > 3:
       break
    print("Sorry, you couldn't guess my birthday")
     
print("Yes, my birthday month is December.") #doubt here

    # Option 2:
for att in [1,2,3]:
    month = input("Guess my birthday month: ").title().strip()
    if month == "December":
        break

# print initial character for every name 
st = ["Tamara", "Antonia", "Arpit", "Pablo", "Anna", "Ishan"]

for n in st:
    print(n[0])
    
# print initial character for every starting with A
for a in st:
    if a[0] == "A":
        print(a[0])

# print name for only the first name 
for a1 in st:
    if a1[0] == "A":
        print(a1)
        break

# print name for only starting with a vowel
for a2 in st:
    if a2[0] in ["A", "E", "I", "O", "U"]:
        print(a2)


#%%
ct = 0
for a3 in st:
    if a3[0] == "A":
        print(a3)
        ct =+1
        if ct != 1:
            continue
    elif a3[0] == "E":
         print(a3)
         ct =+1
         if ct == 1:
            break
    elif a3[0] == "I":
         print(a3)
         ct =+1
         if ct == 1:
            continue
    elif a3[0] == "O":
         print(a3)
         ct =+1
         if ct == 1:
            continue
    elif a3[0] == "U":
         print(a3)
         ct =+1
         if ct == 1:
            continue