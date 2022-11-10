#Two Modes Calculator
#-----------------------

import os 
import time 

L1 = True
while L1:
	print("---------------------------------")
	print("To Enter Standard Mode   ---->  Press 1")
	print("To Enter Programmer Mode ---->  press 2")
	print("---------------------------------")

	mode = int(input("Enter Your Choise: "))
	print("---------------------------------")
	os.system("cls")

	LS = True
	LT = True
	
	if mode == 1 :
		while LS :
			print("*"*5," Welcome To Standard Mode ","*"*5)
			print("---------------------------------")
			N1 = int(input("Enter First Number : "))
			N2 = int(input("Enter Second Number: "))
			print("---------------------------------")
			print("Addition    --->  Press 1")
			print("Subtraction --->  Press 2")
			print("Multiply    --->  Press 3")
			print("Division    --->  Press 4")
			print("Reminder    --->  Press 5")
			
			print("---------------------------------")
			select1 = int(input("Enter Your Choise: "))
			print("---------------------------------")
			os.system("cls")
			
			if select1 == 1 :
				print("The Addition: {} + {} = {} \n".format(N1,N2,N1+N2))
				time.sleep(2)
				
			elif select1 == 2 :
				print("The Subtraction: {} - {} = {} \n".format(N1,N2,N1-N2))
				time.sleep(2)
				
			elif select1 == 3 :
				print("The Multiplication: {} * {} = {} \n".format(N1,N2,N1*N2))
				time.sleep(2)
				
			elif select1 == 4 :
				print("The Division: {} / {} = {} \n".format(N1,N2,N1/N2))
				time.sleep(2)
				
			elif select1 == 5 :
				print("The Reminder: {} % {} = {} \n".format(N1,N2,N1%N2))
				time.sleep(2)
			
			else :
				print("Invalid Choise !! ")
				time.sleep(1)
			print("Do You Want To Do another Operation ? ---> Y - N")
			Ch1 = input("Enter Your Choise: ")
			if Ch1 == 'n' or Ch1 == 'N' :
				LS = False
			os.system("cls")

			

				
			
#-----------------------------------------------------------------------------------

	elif mode == 2 :

		while LT :
			print("*"*5,"Programmer Mode","*"*5)
			print("---------------------------------")
			N1 = int(input("Enter First Number : "))
			N2 = int(input("Enter Second Number: "))
			print("---------------------------------")
		
			print("AND Operator  --->  Press 1")
			print("OR  Operator  --->  Press 2")
			print("NOT Operator  --->  Press 3")
			print("XOR Operator  --->  Press 4")
			print("Shift Right   --->  Press 5")
			print("Shift Left    --->  press 6")
			
			print("---------------------------------")
			select2 = int(input("Enter Your Choise: "))
			print("---------------------------------")
			
			if select2 == 1 :
				os.system("cls")
				print("AND Operation: {} & {} In Decimal Form = {} ".format(N1,N2,N1&N2))
				print("---------------------------------")
				print("AND Operation: {} & {} In Binary Form = {} ".format(bin(N1),bin(N2),bin(N1&N2)))
				print("---------------------------------")
				time.sleep(2)
				
			elif select2 == 2 :
				os.system("cls")
				print("OR Operation: {} | {} In Decimal Form = {} ".format(N1,N2,N1|N2))		
				print("---------------------------------")
				print("OR Operation: {} | {} In Binary Form = {} ".format(bin(N1),bin(N2),bin(N1|N2)))
				print("---------------------------------")
				time.sleep(2)
				
			elif select2 == 3 :
				os.system("cls")
				print("If You Want NOT Operation On First Number   Press 1")
				print("If You Want NOT Operation On Second Number  Press 2")
				print("---------------------------------")
				op1 = int(input("Enter Your Choise: "))
				print("---------------------------------")
				
				if op1 == 1 :
					os.system("cls")
					print("NOT Operation On First Number: ~{} In Decimal Form = {} ".format(N1,~N1))
					print("---------------------------------")
					print("NOT Operation On First Number: ~{} In Binary Form = {} ".format(bin(N1),bin(~N1)))
					print("---------------------------------")
					time.sleep(2)
					
				elif op1 == 2 :
					os.system("cls")
					print("NOT Operation On Second Number: ~{} In Decimal Form = {} ".format(N2,~N2))
					print("---------------------------------")
					print("NOT Operation On Second Number: ~{} In Binary Form = {} ".format(bin(N2),bin(~N2)))
					print("---------------------------------")
					time.sleep(2)
					
			elif select2 == 4 :
				os.system("cls")
				print("XOR Operation: {} ^ {} In Decimal Form = {} ".format(N1,N2,N1^N2))
				print("---------------------------------")
				print("XOR Operation: {} ^ {} In Binary  Form = {} ".format(bin(N1),bin(N2),bin(N1^N2)))
				print("---------------------------------")
				time.sleep(2)
				
			elif select2 == 5 :
				os.system("cls")
				print("If You Want R-Shift Operation On First Number  --->   Press 1")
				print("If You Want R-Shift Operation On Second Number --->   Press 2")
				print("---------------------------------")
				op2 = int(input("Enter Your Choise: "))
				print("---------------------------------")
				sh1 = int(input("Enter Number Of Shifts You Want: "))
				print("---------------------------------")
				
				if op2 == 1 :
					print("R-Shift Operation On First Number: {} >> {} In Decimal Form = {} ".format(N1,sh1,N1>>sh1))
					print("---------------------------------")
					print("R-Shift Operation On First Number: {} >> {} In Binary Form = {} ".format(bin(N1),sh1,bin(N1>>sh1)))
					print("---------------------------------")
					time.sleep(2)
					
				elif op2 == 2 :
					print("R-Shift Operation On Second Number: {} >> {} In Decimal Form = {} ".format(N2,sh1,N2>>sh1))
					print("---------------------------------")
					print("R-Shift Operation On Second Number: {} >> {} In Binary Form = {} ".format(bin(N2),sh1,bin(N2>>sh1)))
					print("---------------------------------")
					time.sleep(2)
					
			elif select2 == 6 :
				os.system("cls")
				print("If You Want L-Shift Operation On First Number   ---> Press 1")
				print("If You Want L-Shift Operation On Second Number  ---> Press 2")
				print("---------------------------------")
				op3 = int(input("Enter Your Choise: "))
				print("---------------------------------")
				sh2 = int(input("Enter Number Of Shifts You Want: "))
				print("---------------------------------")
				
				if op3 == 1 :
					print("L-Shift Operation On First Number: {} << {} In Decimal Form = {} ".format(N1,sh2,N1<<sh2))
					print("---------------------------------")
					print("L-Shift Operation On First Number: {} << {} In Binary Form = {} ".format(bin(N1),sh2,bin(N1<<sh2)))
					print("---------------------------------")
					time.sleep(2)
					
				elif op3 == 2 :
					print("L-Shift Operation On Second Number: {} << {} In Decimal Form = {} ".format(N2,sh2,N2<<sh2))
					print("---------------------------------")
					print("L-Shift Operation On Second Number: {} << {} In Binary Form = {} ".format(bin(N2),sh2,bin(N2<<sh2)))
					print("---------------------------------")
					time.sleep(2)
			
			else :
				print("Invalid Choise !! ")
				print("---------------------------------")
				time.sleep(1)
			print("Do You Want To Do another Operation ? ---> Y - N")
			Ch2 = input("Enter Your Choise: ")
			if Ch2 == 'n' or Ch2 == 'N' :
				LT = False
			os.system("cls")
			
				
		
#-----------------------------------------------------------------------------------
	else :
		print("Invalid Choise Please Try Again !! ")
		print("---------------------------------")
		time.sleep(2)
		os.system("cls")
	
		
