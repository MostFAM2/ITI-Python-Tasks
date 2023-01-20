#--------------------------------------------------------------------------
# @File			:	Calculator_Task.py
# @Author		:	Mostafa Mahmoud 
# @Brief		:	Program To  Simulate Calculator With Two Modes
#--------------------------------------------------------------------------

import os 
import time 

L1 = True
while L1:
	print("---------------------------------")
	print("To Enter Standard Mode   ---->  Press 1")
	print("To Enter Programmer Mode ---->  press 2")
	print("---------------------------------")

	mode = int(input("Enter Your Choice: "))
	print("---------------------------------")
	os.system("cls")

	LS = True
	LT = True
 
	if mode == 1 :
		while LS :
			print("-"*10," (Welcome To Standard Mode) ","-"*10)
			print("-"*50)
   
			N1 = int(input("Enter First Number : "))
			N2 = int(input("Enter Second Number: "))
			print("---------------------------------")
   
			print("Addition    --->  Press 1")
			print("Subtraction --->  Press 2")
			print("Multiply    --->  Press 3")
			print("Division    --->  Press 4")
			print("Reminder    --->  Press 5")
			print("---------------------------------")
   
			select1 = int(input("Enter Your Choice: "))
			print("---------------------------------")
			
			if select1 == 1 :
				print(f"Addition: {N1} + {N2} = {N1+N2} \n")
				time.sleep(2)
    
			elif select1 == 2 :
				print(f"Subtraction: {N1} - {N2} = {N1-N2} \n")
				time.sleep(2)
    
			elif select1 == 3 :
				print(f"Multiplication: {N1} * {N2} = {N1*N2} \n")
				time.sleep(2)
    	
			elif select1 == 4 :
				print(f"Division: {N1} / {N2} = {N1/N2} \n")
				time.sleep(2)
    
			elif select1 == 5 :
				print(f"Reminder: {N1} % {N2} = {N1%N2} \n")
				time.sleep(2)
    
			else :
				print("Invalid Choice !! ")
				time.sleep(2)
    
			print("Do You Want To Do another Operation ? (Y - N)  : ")
			Ch1 = input("Enter Your Choice: ").strip().upper()
   
			if Ch1 == 'N' :
				LS = False
			os.system("cls")		
#----------------------------------------------------------------------------------
# ------------------------------- Programmer Mode --------------------------------
#----------------------------------------------------------------------------------
	
	elif mode == 2 :
		while LT :
			print("-"*9 , " (Welcome To Programmer Mode) " , "-"*9)
			print("-"*50)
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
   
			select2 = int(input("Enter Your Choice: "))
			print("---------------------------------")
			
			if select2 == 1 :
				print(f"AND Operation: {N1} & {N2} In Decimal Form = {N1&N2} ")
				print("-------------------------------------------------------------------")
				print(f"AND Operation: {bin(N1)} & {bin(N2)} In Binary Form  = {bin(N1&N2)} ")
				print("-------------------------------------------------------------------")
				time.sleep(2)
				
			elif select2 == 2 :
				print(f"OR Operation: {N1} | {N2} In Decimal Form = {N1|N2} ")		
				print("-------------------------------------------------------------------")
				print(f"OR Operation: {bin(N1)} | {bin(N2)} In Binary Form  = {bin(N1|N2)} ")
				print("-------------------------------------------------------------------")
				time.sleep(2)
				
			elif select2 == 3 :
				print("If You Want NOT Operation On First Number   Press 1")
				print("If You Want NOT Operation On Second Number  Press 2")
				print("-------------------------------------------------------------------")
    
				op1 = int(input("Enter Your Choice: "))
				print("-------------------------------------------------------------------")
				
				if op1 == 1 :
					print(f"NOT Operation On First Number: ~{N1} In Decimal Form = {~N1} ")
					print("-------------------------------------------------------------------")
					print(f"NOT Operation On First Number: ~{bin(N1)} In Binary Form = {bin(~N1)} ")
					print("-------------------------------------------------------------------")
					time.sleep(2)
					
				elif op1 == 2 :
					print(f"NOT Operation On Second Number: ~{N2} In Decimal Form = {~N2} ")
					print("-------------------------------------------------------------------")
					print(f"NOT Operation On Second Number: ~{bin(N2)} In Binary Form = {bin(~N2)}")
					print("-------------------------------------------------------------------")
					time.sleep(2)
					
			elif select2 == 4 :
				print(f"XOR Operation: {N1} ^ {N2} In Decimal Form = {N1^N2} ")
				print("-------------------------------------------------------------------")
				print(f"XOR Operation: {bin(N1)} ^ {bin(N2)} In Binary  Form = {bin(N1^N2)} ")
				print("-------------------------------------------------------------------")
				time.sleep(2)
				
			elif select2 == 5 :
				print("If You Want R-Shift Operation On First Number  --->   Press 1")
				print("If You Want R-Shift Operation On Second Number --->   Press 2")
				print("-------------------------------------------------------------------")
				op2 = int(input("Enter Your Choice: "))
				print("-------------------------------------------------------------------")
				sh1 = int(input("Enter Number Of Shifts You Want: "))
				print("-------------------------------------------------------------------")
				
				if op2 == 1 :
					print(f"R-Shift Operation On First Number: {N1} >> {sh1} In Decimal Form = {N1>>sh1} ".format(N1,sh1,))
					print("-------------------------------------------------------------------")
					print(f"R-Shift Operation On First Number: {bin(N1)} >> {sh1} In Binary Form = {bin(N1>>sh1)} ")
					print("-------------------------------------------------------------------")
					time.sleep(2)
					
				elif op2 == 2 :
					print(f"R-Shift Operation On Second Number: {N2} >> {sh1} In Decimal Form = {N2>>sh1} ")
					print("-------------------------------------------------------------------")
					print(f"R-Shift Operation On Second Number: {bin(N2)} >> {sh1} In Binary Form = {bin(N2>>sh1)} ")
					print("-------------------------------------------------------------------")
					time.sleep(2)
					
			elif select2 == 6 :
				print("If You Want L-Shift Operation On First Number   ---> Press 1")
				print("If You Want L-Shift Operation On Second Number  ---> Press 2")
				print("-------------------------------------------------------------------")
				op3 = int(input("Enter Your Choice: "))
				print("-------------------------------------------------------------------")
				sh2 = int(input("Enter Number Of Shifts You Want: "))
				print("-------------------------------------------------------------------")
				
				if op3 == 1 :
					print(f"L-Shift Operation On First Number: {N1} << {sh2} In Decimal Form = {N1<<sh2} ")
					print("-------------------------------------------------------------------")
					print(f"L-Shift Operation On First Number: {bin(N1)} << {sh2} In Binary Form = {bin(N1<<sh2)} ")
					print("-------------------------------------------------------------------")
					time.sleep(2)
					
				elif op3 == 2 :
					print(f"L-Shift Operation On Second Number: {N2} << {sh2} In Decimal Form = {N2<<sh2} ")
					print("-------------------------------------------------------------------")
					print(f"L-Shift Operation On Second Number: {bin(N2)} << {sh2} In Binary Form = {bin(N2<<sh2)} ")
					print("-------------------------------------------------------------------")
					time.sleep(2)
			
			else :
				print("Invalid Choice !! ")
				print("-------------------------------------------------------------------")
				time.sleep(1)
    
			print("Do You Want To Do another Operation ? (Y - N) :  ")
			Ch2 = input("Enter Your Choice: ").strip().upper()
   
			if Ch2 == 'N' :
				LT = False
			os.system("cls")
			
				
		
#-----------------------------------------------------------------------------------
	else :
		print("Invalid Choice Please Try Again !! ")
		print("---------------------------------")
		time.sleep(2)
		os.system("cls")
	
		
