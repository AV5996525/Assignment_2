#Name:          Assignment_2.py
#Author:        AJ Varatharajan
#Date Created:  February 28, 2023
#Date Last Modified: March 4, 2023
#Purpose: 
#This program will accept user input to fill out fields regarding their personal information.
#The user will be able to select multiple items. 
#program will ask user to confirm their order and student status. It will prompt for an appropriate entry using y, Y, n, N only.
#If user does not confirm the order, they CAN re enter their selection.
#A receipt will be outputted once the user completes the order.
new_list = [] #intitalizing empty list
custInfo = {"Name":[], "Phone":[], "City":[], "Province":[], "Postal Code":[], "Address":[],"Instructions":[]} #dictionary for customer information
custInfo["Name"].append(input("Enter your name:"))  #Accepting input for customer information dictionary 
custInfo["Phone"].append(input("Enter your phone number:"))
custInfo["City"].append(input("Enter your current city:"))
custInfo["Province"].append(input("Enter your current province:"))
custInfo["Postal Code"].append(input("Enter your current postal code:"))
custInfo["Address"].append(input("Enter your current address:"))
custInfo["Instructions"].append(input("Enter your requests if applicable:"))
from tabulate import tabulate
def mm (): # creating main menu function
    new_list = []
    
    
    
    cOrderSel = str(input("Welcome friends").strip())    #order selection and user input
    if cOrderSel == '1' : 
        cOrderTotal1["Name"].append("Grilled cheese") #adding entry to dictionary for order selection 
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
    if cOrderSel == "C" or cOrderSel == "c":
        
       
        new_list = list(set(cOrderTotalX)) #removing duplicate by converting to set then list

        print(new_list)
        while True: #intializing loop to prompt valid input
            confirm1 = input("Are you sure you want to check out")
            
            if confirm1 == "Y" or confirm1 == "y":
                subT = 0
                final = (((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])) + ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])) + ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])) + ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])) + ((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])) + ((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine'])))
                delivy(x = final)   
                continue
                
            elif confirm1 == "N" or confirm1 == "n" :            
                mm() 
            elif confirm1.isdigit() :
                print("Invalid response. No numbers!")   
            elif confirm1 != "N" and confirm1 != "n" and confirm1 != "Y" or confirm1 != "y":     
                print("Invalid response, please select choice 'Y' or 'N'.")
    elif cOrderSel.isalpha() :
        print("Invalid response. No letters!")
    elif cOrderSel != '1' and cOrderSel != '2' and cOrderSel != '3' and cOrderSel != '4' and cOrderSel != '5' and cOrderSel != '6':
        print("Invalid response, please select choice 1,2,3,4,5,6.")
    
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

 while True :
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
               
                headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                CT1 = ''
                for key in cOrderTotal1["Name"]:
                    if key not in CT1:
                        CT1 = key
                CT2 = ''
                for key in cOrderTotal2["Name"]:
                    if key not in CT2:
                        CT2 = key
                CT3 = ''
                for key in cOrderTotal3["Name"]:
                    if key not in CT3:
                        CT3 = key
                CT4 = ''
                for key in cOrderTotal4["Name"]:
                    if key not in CT4:
                        CT4 = key
                CT5 = ''
                for key in cOrderTotal5["Name"]:
                    if key not in CT5:
                        CT5 = key
                CT6 = ''
                for key in cOrderTotal6["Name"]:
                    if key not in CT6:
                        CT6 = key
                
                amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                table = zip(amp, mass, period, ecc)
                custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                print(tabulate(custInfo, headers = custHead))
                print(tabulate(table, headers=headers, floatfmt=".2f"))
                
                print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand), str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
                
            elif (subT) >= 100 and 500 > (subT) :
                discnt10 = (.10*(subT))
                print("Enjoy a 10% discount on orders over $100 & a waived delivery charge of $5!")
                grand = ((subT) - discnt10 -5)
                
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                tipC(tip,subT)
                taxTime(grand)
                headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                CT1 = ''
                for key in cOrderTotal1["Name"]:
                    if key not in CT1:
                        CT1 = key
                CT2 = ''
                for key in cOrderTotal2["Name"]:
                    if key not in CT2:
                        CT2 = key
                CT3 = ''
                for key in cOrderTotal3["Name"]:
                    if key not in CT3:
                        CT3 = key
                CT4 = ''
                for key in cOrderTotal4["Name"]:
                    if key not in CT4:
                        CT4 = key
                CT5 = ''
                for key in cOrderTotal5["Name"]:
                    if key not in CT5:
                        CT5 = key
                CT6 = ''
                for key in cOrderTotal6["Name"]:
                    if key not in CT6:
                        CT6 = key
              
                amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                table = zip(amp, mass, period, ecc)
                custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                print(tabulate(custInfo, headers = custHead))
                print(tabulate(table, headers=headers, floatfmt=".2f"))
                
                print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
            
            elif (subT) < 500 :
                if subT > 30:
                    discnt5 = (.05*(subT))
                    grand = ((subT) - discnt5 -5)
                    print("Enjoy a 5% discount on orders under $100 & a waived delivery charge of $5!")
                    tip = float(input("Tip the delivery person 10, 15, or 20%"))
                    tipC(tip,subT)
                    taxTime(grand)
                    headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                    CT1 = ''
                    for key in cOrderTotal1["Name"]:
                        if key not in CT1:
                            CT1 = key
                    CT2 = ''
                    for key in cOrderTotal2["Name"]:
                        if key not in CT2:
                            CT2 = key
                    CT3 = ''
                    for key in cOrderTotal3["Name"]:
                        if key not in CT3:
                            CT3 = key
                    CT4 = ''
                    for key in cOrderTotal4["Name"]:
                        if key not in CT4:
                            CT4 = key
                    CT5 = ''
                    for key in cOrderTotal5["Name"]:
                        if key not in CT5:
                            CT5 = key
                    CT6 = ''
                    for key in cOrderTotal6["Name"]:
                        if key not in CT6:
                            CT6 = key
                    
                    amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                    mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                    period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                    ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                    table = zip(amp, mass, period, ecc)
                    custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                    print(tabulate(custInfo, headers = custHead))
                    print(tabulate(table, headers=headers, floatfmt=".2f"))
                    
                    print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
                if subT < 30:
                    discnt5 = (.05*(subT))
                    grand = ((subT) - discnt5 + 5)
                    print("Enjoy a 5% discount on orders under $100")
                    tip = float(input("Tip the delivery person 10, 15, or 20%"))
                    tipC(tip,subT)
                    taxTime(grand)
                    headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                    CT1 = ''
                    for key in cOrderTotal1["Name"]:
                        if key not in CT1:
                            CT1 = key
                    CT2 = ''
                    for key in cOrderTotal2["Name"]:
                        if key not in CT2:
                            CT2 = key
                    CT3 = ''
                    for key in cOrderTotal3["Name"]:
                        if key not in CT3:
                            CT3 = key
                    CT4 = ''
                    for key in cOrderTotal4["Name"]:
                        if key not in CT4:
                            CT4 = key
                    CT5 = ''
                    for key in cOrderTotal5["Name"]:
                        if key not in CT5:
                            CT5 = key
                    CT6 = ''
                    for key in cOrderTotal6["Name"]:
                        if key not in CT6:
                            CT6 = key
                  
                    amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                    mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                    period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                    ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                    table = zip(amp, mass, period, ecc)
                    custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                    print(tabulate(custInfo, headers = custHead))
                    print(tabulate(table, headers=headers, floatfmt=".2f"))
                    
                    print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
                    
        if deliv == "N" :
            
            subT = (x) 
            if (subT) > 500:
                discnt15 = (.15*(subT))
                print("Enjoy a 15% discount on orders over $500")
                grand = ((subT) - discnt15)
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                taxTime(grand)
                headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                CT1 = ''
                for key in cOrderTotal1["Name"]:
                    if key not in CT1:
                        CT1 = key
                CT2 = ''
                for key in cOrderTotal2["Name"]:
                    if key not in CT2:
                        CT2 = key
                CT3 = ''
                for key in cOrderTotal3["Name"]:
                    if key not in CT3:
                        CT3 = key
                CT4 = ''
                for key in cOrderTotal4["Name"]:
                    if key not in CT4:
                        CT4 = key
                CT5 = ''
                for key in cOrderTotal5["Name"]:
                    if key not in CT5:
                        CT5 = key
                CT6 = ''
                for key in cOrderTotal6["Name"]:
                    if key not in CT6:
                        CT6 = key
               
                amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                table = zip(amp, mass, period, ecc)
                custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                print(tabulate(custInfo, headers = custHead))
                print(tabulate(table, headers=headers, floatfmt=".2f"))
                
                print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
            elif (subT) >= 100 and 500 > (subT) :
                discnt10 = (.10*(subT))
                grand = ((subT) - discnt10)
                print("Enjoy a 10% discount on orders over $100")
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                taxTime(grand)
                headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                CT1 = ''
                for key in cOrderTotal1["Name"]:
                    if key not in CT1:
                        CT1 = key
                CT2 = ''
                for key in cOrderTotal2["Name"]:
                    if key not in CT2:
                        CT2 = key
                CT3 = ''
                for key in cOrderTotal3["Name"]:
                    if key not in CT3:
                        CT3 = key
                CT4 = ''
                for key in cOrderTotal4["Name"]:
                    if key not in CT4:
                        CT4 = key
                CT5 = ''
                for key in cOrderTotal5["Name"]:
                    if key not in CT5:
                        CT5 = key
                CT6 = ''
                for key in cOrderTotal6["Name"]:
                    if key not in CT6:
                        CT6 = key
                
                amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                table = zip(amp, mass, period, ecc)
                custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                print(tabulate(custInfo, headers = custHead))
                print(tabulate(table, headers=headers, floatfmt=".2f"))
                
                print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
            elif (subT) < 500 :
                discnt5 = (.05*(subT))
                grand = ((subT) - discnt5)
                print("Enjoy a 5% discount on orders under $100")
                tip = float(input("Tip the delivery person 10, 15, or 20%"))
                taxTime(grand)
                headers = ['Items', 'Quantity', 'Unit Price', 'Sub Total']    #tabulate
                CT1 = ''
                for key in cOrderTotal1["Name"]:
                    if key not in CT1:
                        CT1 = key
                CT2 = ''
                for key in cOrderTotal2["Name"]:
                    if key not in CT2:
                        CT2 = key
                CT3 = ''
                for key in cOrderTotal3["Name"]:
                    if key not in CT3:
                        CT3 = key
                CT4 = ''
                for key in cOrderTotal4["Name"]:
                    if key not in CT4:
                        CT4 = key
                CT5 = ''
                for key in cOrderTotal5["Name"]:
                    if key not in CT5:
                        CT5 = key
                CT6 = ''
                for key in cOrderTotal6["Name"]:
                    if key not in CT6:
                        CT6 = key
                
                amp = [CT1,CT2,CT3,CT4,CT5,CT6]
                mass = [sum(cOrderTotal1["Quantity"]), sum(cOrderTotal2["Quantity"]), sum(cOrderTotal3["Quantity"]), sum(cOrderTotal4["Quantity"]), sum(cOrderTotal5["Quantity"]), sum(cOrderTotal6["Quantity"])]    
                period = [(items[1]['Grilled cheese']), (items[2]['Hot dog']), (items[3]['Sushi']), (items[4]['Butter chicken']),(items[5]['Greek salad']),(items[6]['Poutine'])]    
                ecc = [((sum(cOrderTotal1["Quantity"])) * (items[1]['Grilled cheese'])), ((sum(cOrderTotal2["Quantity"])) * (items[2]['Hot dog'])), ((sum(cOrderTotal3["Quantity"])) * (items[3]['Sushi'])), ((sum(cOrderTotal4["Quantity"])) * (items[4]['Butter chicken'])),((sum(cOrderTotal5["Quantity"])) * (items[5]['Greek salad'])),((sum(cOrderTotal6["Quantity"])) * (items[6]['Poutine']))]                         
                table = zip(amp, mass, period, ecc)
                custHead = ["Name", "Phone", "City", "Province", "Postal", "Address","Requests"]
                print(tabulate(custInfo, headers = custHead))
                print(tabulate(table, headers=headers, floatfmt=".2f"))
                
                print(tabulate([[ str(tipC(tip,subT)), str(taxTime(grand)), str(grand),str(taxTime(grand)+tipC(tip,subT)+grand)]], headers = ['Tip','Tax', 'Total','Grand Total'],floatfmt=".2f"))
            break
        elif deliv.isdigit() :
                print("Invalid response. No numbers!")   
        elif deliv != "N" and deliv != "n" and deliv != "Y" and deliv != "y":     
                print("Invalid response, please select choice 'Y' or 'N'.")
        
        return  taxTime, tipC 


items = {}
items = {
    1: {"Grilled cheese": 14.00},
    2: {"Hot dog" : 15.00},
    3: {"Sushi" : 17.00},
    4: {"Butter chicken" : 18.00},
    5: {"Greek salad" : 16.00},
    6: {"Poutine" : 12.00},
}

cOrderTotal1 = {"Name":[],"Quantity":[]}
cOrderTotal2 = {"Name":[],"Quantity":[]}
cOrderTotal3 = {"Name":[],"Quantity":[]}
cOrderTotal4 = {"Name":[],"Quantity":[]}
cOrderTotal5 = {"Name":[],"Quantity":[]}
cOrderTotal6 = {"Name":[],"Quantity":[]}
cOrderTotalX = []



while True:
    mm()
    