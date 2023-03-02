#final = (sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])

#print(final)

#print(items[2]['Hot dog'])

#def gc () : 
    #cOrderTotal["Name"].append("Grilled Cheese")
    #cOrderTotal["Quantity"].append(1)
    #print(cOrderTotal)
    #return cOrderTotal
dc = 5
def delivy (x) :
    deliv = input("Would you like to have this order delivered?")
    if deliv == "Y" :
        subT = dc + (x)
    if deliv == "N" :
        subT = (x) - dc
    print(subT)    
    return subT
def discount (y):
    if y > 500:
        discnt15 = (.15*y)
        grand15 = (y - discnt15)
    elif y >= 100 and 500 > y :
        discnt10 = (.10*y)
        grand10 = (y - discnt10)
    elif y < 500 :
        discnt5 = (.05*y)
        grand5 = (y - discnt5)
    return grand15, grand10, grand5
cOrderTotal = {}

items = {}
items = {
    1: {"Grilled cheese": 10.00},
    2: {"Hot dog" : 5.00},
    3: {"Sushi" : 7.00},
    4: {"Butter chicken" : 8.00},
    5: {"Greek salad" : 6.00},
    6: {"Poutine" : 5.00},
}

cOrderTotal1 = {"Name":[],"Quantity":[]}
cOrderTotal2 = {"Name":[],"Quantity":[]}
cOrderTotal3 = {"Name":[],"Quantity":[]}
cOrderTotal4 = {"Name":[],"Quantity":[]}
cOrderTotal5 = {"Name":[],"Quantity":[]}
cOrderTotal6 = {"Name":[],"Quantity":[]}

def mm ():
    cOrderSel = str(input("Welcome friends"))    
    if cOrderSel == '1' : 
        cOrderTotal1["Name"].append("Grilled cheese")
        cOrderTotal1["Quantity"].append(1)
    if cOrderSel == '2' : 
        cOrderTotal2["Name"].append("Hot dog")
        cOrderTotal2["Quantity"].append(1)
        print(str(cOrderTotal2))
    if cOrderSel == '3' : 
        cOrderTotal3["Name"].append("Sushi")
        cOrderTotal3["Quantity"].append(1)
    if cOrderSel == '4' : 
        cOrderTotal4["Name"].append("Butter chicken")
        cOrderTotal4["Quantity"].append(1)
    if cOrderSel == '5' : 
        cOrderTotal5["Name"].append("Greek salad")
        cOrderTotal5["Quantity"].append(1)
    if cOrderSel == '6' :
        cOrderTotal6["Name"].append("Poutine")
        cOrderTotal6["Quantity"].append(1)
    if cOrderSel == "C" :
        confirm1 = input("Are you sure you want to check out")
        if confirm1 == "Y":
            subT = ''
            final = (((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])) + ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])) + ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])) + ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])) + ((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])) + ((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine'])))
            delivy(x = final)
            discount(y=subT)
        elif confirm1 == "N":            
            mm() 
    return cOrderTotal1, cOrderTotal2, cOrderTotal3, cOrderTotal4, cOrderTotal5, cOrderTotal6
    

while True:
    mm()
