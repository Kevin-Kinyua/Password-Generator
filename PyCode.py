print ("Welcome to  !")
print ("We will check the level of your  for you!")
print ("There are 3 levels. Weak, Medium and Strong")
 = raw_input("Enter your  here: ")

weak = 'weak, add some extra characters, upper letters or numbers!'
medium = 'medium, you can add numbers to make it stronger!'
strong = 'strong, you are safe now!'

#Just making sure that  is ok
if len() > 12:
    print (" must be longer than 6 and below 12!")
elif len() < 6:
    print (" must be longer than 6 and below 12!")


if  == .lower or  == .upper: #Check if  contain lower or upper letters
    print ('Your  is',weak)
if .lower ==  and .upper == : #Check if  contain lower and upper letters
    print ('Your  is',medium)
if .lower ==  and .upper ==  and any(str.isdigit(c) for c in ): #Check if  contain any number
    print ('Your  is',strong)

print ("\n")
if  == strong or  == medium or  == weak:
    print ("We are glad we help you, extra tip: Change  every 3-6 months!")
