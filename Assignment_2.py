#final = (sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])

#print(final)



#def gc () : 
    #cOrderTotal["Name"].append("Grilled Cheese")
    #cOrderTotal["Quantity"].append(1)
    #print(cOrderTotal)
    #return cOrderTotal
new_list = []
from tabulate import tabulate
def mm ():
    new_list = []
    
    cOrderSel = str(input("Welcome friends"))    
    if cOrderSel == '1' : 
        cOrderTotal1["Name"].append("Grilled cheese")
        a = int(input("How many"))
        
        cOrderTotal1["Quantity"].append(a)
        if a > 0:
            
            cOrderTotalX.append("Grilled cheese")
    if cOrderSel == '2' : 
        cOrderTotal2["Name"].append("Hot dog")
        b = int(input("How many"))
        cOrderTotal2["Quantity"].append(b)
        print(str(cOrderTotal2))
        if b > 0:
           
            cOrderTotalX.append("Hot dog")
    if cOrderSel == '3' : 
        cOrderTotal3["Name"].append("Sushi")
        c = int(input("How many"))
        cOrderTotal3["Quantity"].append(c)
        if c > 0:
            
            cOrderTotalX.append("Sushi")
    if cOrderSel == '4' : 
        cOrderTotal4["Name"].append("Butter chicken")
        d = int(input("How many"))
        cOrderTotal4["Quantity"].append(d)
        if d > 0:
            
            cOrderTotalX.append("Butter chicken")
    if cOrderSel == '5' : 
        cOrderTotal5["Name"].append("Greek salad")
        e = int(input("How many"))
        cOrderTotal5["Quantity"].append(e)
        if e > 0:
            
            cOrderTotalX.append("Greek salad")
    if cOrderSel == '6' :
        cOrderTotal6["Name"].append("Poutine")
        f = int(input("How many"))
        cOrderTotal6["Quantity"].append(f)
        if f > 0:
           
            cOrderTotalX.append("Poutine")
    if cOrderSel == "C" :
        
       
        new_list = list(set(cOrderTotalX)) #removing duplicate by converting to set then list

        print(new_list)

        confirm1 = input("Are you sure you want to check out")
        
        if confirm1 == "Y":
            subT = 0
            final = (((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])) + ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])) + ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])) + ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])) + ((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])) + ((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine'])))
            delivy(x = final)   
            
            
        elif confirm1 == "N":            
            mm() 
    return cOrderTotal1, cOrderTotal2, cOrderTotal3, cOrderTotal4, cOrderTotal5, cOrderTotal6, new_list, taxTime, tipC   
def taxTime(L):
    hst = .13
    tax = (L) * hst
    
    return tax
def tipC(J,K):
    if (J) == 10 :
        tipA = .10 * (K) 
    if (J) == 15 :
        tipA = .15 * (K) 
    if (J) == 20 :
        tipA = .20 * (K)
    
    return tipA 
def delivy (x) :
    
    deliv = input("Would you like to have this order delivered?")
    if deliv == "Y" :
        subT =  (x)
        if (subT) > 500:
            discnt15 = (.15*(subT))
            print("Enjoy a 15% discount on orders over $500 & a waived delivery charge of $5!")
            grand = ((subT) - discnt15 -5) 
            
            tip = float(input("Tip the delivery person 10, 15, or 20%"))
            tipC(tip,subT)
            
            taxTime(grand)
            new_listZ = list(set(cOrderTotalX))
            new_listZ.sort()
            #[et.split(',')[0] for et in new_listZ]
            headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate

            amp = [(cOrderTotal1["Name"][0]), (cOrderTotal2["Name"][0]), (cOrderTotal3["Name"][0]), (cOrderTotal4["Name"][0]), (cOrderTotal5["Name"][0]), (cOrderTotal6["Name"][0])]
            mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
            period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
            ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
            table = zip(amp, mass, period, ecc)
            print(tabulate(table, headers=headers, floatfmt=".2f"))
            #headers2 = ['Tip','Tax', 'Grand Total']
            #table2 = zip( str(tipC(tip,subT)), str(taxTime(grand)), str(grand))
            #print(tabulate(str(tipC(tip,subT)), headers=headers2, floatfmt=".2f"))
            print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total']))
        elif (subT) >= 100 and 500 > (subT) :
            discnt10 = (.10*(subT))
            print("Enjoy a 10% discount on orders over $100 & a waived delivery charge of $5!")
            grand = ((subT) - discnt10 -5)
            
            tip = float(input("Tip the delivery person 10, 15, or 20%"))
            tipC(tip,subT)
            taxTime(grand)
           
        elif (subT) < 500 :
            if subT > 30:
                discnt5 = (.05*(subT))
                grand = ((subT) - discnt5 -5)
                print("Enjoy a 5% discount on orders under $100 & a waived delivery charge of $5!")
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                tipC(tip,subT)
                taxTime(grand)
                
            if subT < 30:
                discnt5 = (.05*(subT))
                grand = ((subT) - discnt5 + 5)
                print("Enjoy a 5% discount on orders under $100")
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                tipC(tip,subT)
                taxTime(grand)
                
                
    if deliv == "N" :
        subT = (x) 
        if (subT) > 500:
            discnt15 = (.15*(subT))
            print("Enjoy a 15% discount on orders over $500")
            grand = ((subT) - discnt15)
            
            taxTime(grand)
        elif (subT) >= 100 and 500 > (subT) :
            discnt10 = (.10*(subT))
            grand = ((subT) - discnt10)
            print("Enjoy a 10% discount on orders over $100")
            taxTime(grand)
        elif (subT) < 500 :
            discnt5 = (.05*(subT))
            grand = ((subT) - discnt5)
            print("Enjoy a 5% discount on orders under $100")
            taxTime(grand)
    
    return float(subT) , taxTime, tipC 

#custInfo = {"Name":[], "Phone":[], "City":[], "Province":[], "Postal Code":[], "Address":[],"Instructions":[]}
#custInfo["Name"].append(input("Enter your name:"))
#custInfo["Phone"].append(input("Enter your name:"))
#custInfo["City"].append(input("Enter your name:"))
#custInfo["Province"].append(input("Enter your name:"))
#custInfo["Postal Code"].append(input("Enter your name:"))
#custInfo["Address"].append(input("Enter your name:"))
#custInfo["Instructions"].append(input("Enter your name:"))
#print(custInfo)
items = {}
items = {
    1: {"Grilled cheese": 14.00},
    2: {"Hot dog" : 15.00},
    3: {"Sushi" : 17.00},
    4: {"Butter chicken" : 18.00},
    5: {"Greek salad" : 16.00},
    6: {"Poutine" : 12.00},
}
#print(items[2]['Hot dog'])
cOrderTotal1 = {"Name":[],"Quantity":[]}
cOrderTotal2 = {"Name":[],"Quantity":[]}
cOrderTotal3 = {"Name":[],"Quantity":[]}
cOrderTotal4 = {"Name":[],"Quantity":[]}
cOrderTotal5 = {"Name":[],"Quantity":[]}
cOrderTotal6 = {"Name":[],"Quantity":[]}
cOrderTotalX = []



while True:
    mm()
    