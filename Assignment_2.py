def gc () : 
    cOrderTotal["Name"].append("Grilled Cheese")
    cOrderTotal["Quantity"].append(1)
    print(cOrderTotal)
    return cOrderTotal
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
print(items[2]['Hot dog'])
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
            final = (sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])
            print(final)
    return cOrderTotal1, cOrderTotal2, cOrderTotal3, cOrderTotal4, cOrderTotal5, cOrderTotal6
    

while True:
    mm()
