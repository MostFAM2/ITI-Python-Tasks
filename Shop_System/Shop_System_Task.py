#--------------------------------------------------------------------------
# @File			:	Shop_System_Task.py
# @Author		:	Mostafa Mahmoud 
# @Brief		:	Program To Manage Market Shop 
#--------------------------------------------------------------------------



''' ITI Shop System '''
#------------------------


''' Data Base Section '''
#------------------------

#This Dict To Know The Available Products
Products = {
			"Product_Name"   : ["Products:" , "Rice" , "Sugar" , "Salt" , "Oil" , "Macaroni" , "Apple" , "Banana" , "Mango" , "Guava"],
			"Product_Price"  : ["Price   :" ,   20,       20,       2,      40,      15,          20,       10,       20,        8],
			"Product_Stock"  : ["Stock   :" ,   10,       10,      20,      10,      20,          10,       10,       10,        20],
			}

#This Dict To Know The Items That The Customer Bought			
Cust_Box = {
			"Type"     : [],				#To Put in The Product
			"Quantity" : [],				#To Put in The Quantity
			"Price"    : [],				#To Put in The Price
			}


import time
import os
import csv 



print("-"*70)
print(" "*10,"*"*7,"Welcome To ITI Shop System","*"*7," "*5)
print("-"*70)


L1 = True
while L1:
	print("For Customers  ----->  Press 1")
	print("For Owner      ----->  Press 2")
	print("-"*30)
	mode = int(input("Enter Your Choice: "))
	print("-"*30)
	os.system("cls")
	
	if mode == 1 :
		LC1 = True 
		while LC1 :
			print("------- Hello Customer -------")
			print("To Buy From Products  ---> Press 1")
			print("To Print Your Bill    ---> Press 2")
			print("To Exit               ---> Press 0")
			print("-"*30)
			
			cust_choice = int(input("Enter Your Choice: "))
			print("-"*30)
			os.system("cls")
			
			if cust_choice == 1 :
				LC = True 
				while LC :
					print("Choose Product")
					print("-"*30)
					print(*Products["Product_Name"], sep=' / ')
					print(*Products["Product_Price"],sep='  / ')
					print("-"*30)
					
					Element = input("Type The Name Of Product You Want: ")
					Cust_Box["Type"].append(Element)
					print("-"*30)
					
					Qun = float(input("How Many Kilo Grams You Want ? ---> "))
					Cust_Box["Quantity"].append(Qun)
					Products["Product_Name"]
					print("-"*30)
					Products["Product_Stock"][Products["Product_Name"].index(Element)] -= Qun
					
					print("-"*30)
					print("Do You Want To Buy Another Product ?  ---> Y - N")
					ag = input("Enter Your Choice: ")
					print("-"*30)	
					os.system("cls")
					
					if ag == 'n' or ag == 'N' :
						LC = False 
			
			elif cust_choice == 2 :
				bills = 0
				for i in range (len(Cust_Box["Type"])) :
					bills += Products["Product_Price"][Products["Product_Name"].index(Cust_Box["Type"][i])] * Cust_Box["Quantity"][i]
				print("Your Bill =  ",end='')
				print(bills)
				time.sleep(5)
				os.system("cls")
						
			elif cust_choice == 0 :
				LC1 = False 
			
			else :
				print("Invalid Choice !! Try Again")
				
		
	
	
	elif mode == 2 :
		checking = 0 
		LO1 = True 
		while checking != 3 :
			print("Please Enter The Password To Access Owner Mode")
			print("-"*30)
			password = int(input("Your Password: "))
			print("-"*30)
			if password == 1996 :
				os.system("cls")
				print("***************Welcome To Owner Mode****************************")
				checking = 3 
				while LO1 :
					print("-"*70)
					print("To Show Available Products On System     ---> Press 1")
					print("To Add New Product TO System             ---> Press 2")
					print("To Change In Product Price On System     ---> Press 3")
					print("To Exit From System                      ---> Press 0")
					print("-"*30)
					own_choice = int(input("Enter Your Choice: "))
					print("-"*30)
									
					if own_choice == 1 :
						os.system("cls")
						print(*Products["Product_Name"], sep=' / ')
						print("-"*30)
						print(*Products["Product_Price"], sep='  /  ')
						print("-"*30)
						print(*Products["Product_Stock"], sep='  /  ')
						print("-"*30)
						time.sleep(2)
									
					elif own_choice == 2 :
						LO = True 
						while LO :
							os.system("cls")
							print("******Please Enter One Element Each Time**********\n")
							New_Ele_Name = input("Type New Element Name: ")
							Products["Product_Name"].append(New_Ele_Name)
							print("-"*30)
							New_Ele_Price = float(input("Enter The Price Of The New Element: "))
							Products["Product_Price"].append(New_Ele_Price)
							print("-"*30)
							New_Ele_Quantity = int(input("Enter Stock Of This New Product: "))
							Products["Product_Stock"].append(New_Ele_Quantity)
							os.system("cls")
							print("-"*30)
							print("Do You Want To Add New Element Again ? ---> Y - N")
							New_Ch = input("Enter Your Choice: ")
							print("-"*30)
							if New_Ch == 'n' or New_Ch == 'N' :
								LO = False
							os.system("cls")
							
				
					elif own_choice == 3 :
						L_Change = True
						while L_Change :
							os.system("cls")
							Change_Price_Ele1 = input("Please Type Name Of The Element You Want To Change Its Price: ")
							Ind_Ele = Products["Product_Name"].index(Change_Price_Ele1)
							print("-"*30)
							Change_Price_Ele2 = float(input("Enter New Price: "))
							Products["Product_Price"].insert(Ind_Ele,Change_Price_Ele2)
							print("-"*30)
							print("Do You Want To Change Price Of Another Element ? ---> Y - N")
							Ch_Check = input("Enter Your Choice: ")
							os.system("cls")
							if Ch_Check == 'N' or Ch_Check == 'n' :
								L_Change = False
							os.system("cls")
				
					elif own_choice == 0 :
						LO1 = False
						os.system("cls")
									
					else :
						print("Invalid Choice !!")
						print("-"*30)
						
			
			else :
				checking += 1
				print("Incorrect Password Try Again")
				print("-"*30)
				 	
	
	else :
		print("Invalid Choice !!")
		print("-"*30)
	
	