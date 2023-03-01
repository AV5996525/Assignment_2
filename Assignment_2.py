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
cOrderTotal = {"Name":[],"Quantity":[]}


def mm ():
    cOrderSel = str(input("Welcome friends"))    
    if cOrderSel == '1' : 
        cOrderTotal["Name"].append("Grilled cheese")
    if cOrderSel == '2' : 
        cOrderTotal["Name"].append("Hot dog")
        cOrderTotal["Quantity"].append(1)
        print(str(cOrderTotal))
    if cOrderSel == '3' : 
        cOrderTotal["Name"].append("Sushi")
    if cOrderSel == '4' : 
        cOrderTotal["Name"].append("Butter chicken")
    if cOrderSel == '5' : 
        cOrderTotal["Name"].append("Greek salad")
    if cOrderSel == '6' :
        cOrderTotal["Name"].append("Poutine")
    return cOrderTotal

while True:
    mm()
