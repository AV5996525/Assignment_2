items = {}
items = {
    1: {"Grilled Cheese": 10.00},
    2: {"Hotdog" : 5.00},
    3: {"Sushi" : 7.00},
    4: {"Butter Chicken" : 8.00},
    5: {"Greek Salad" : 6.00},
    6: {"Poutine" : 5.00},
}
#print(items[2]['Hotdog'])
cOrderSel = {}
cOrderSel = input().split(",")    
val = ''    
for x in cOrderSel:
    val = dict.fromkeys(items,x)


print(val)