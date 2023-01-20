from tkinter import *
from PIL import ImageTk, Image
from PIL import Image
# import pygame

''' To Count Number Of Large Cups '''
def LargeButtonPress ():
    LargeButtonPress.count += 1 
    print("The Large Button is Pressed: " , LargeButtonPress.count)
LargeButtonPress.count = 0 
''' ======================================================= '''

''' To Count Number Of Medium Cups '''
def MediumButtonPress ():
    MediumButtonPress.count += 1 
    print("The Medium Button is Pressed: " , MediumButtonPress.count)
MediumButtonPress.count = 0 
''' ======================================================= '''

''' To Count Number Of Small Cups '''
def SmallButtonPress ():
    SmallButtonPress.count += 1 
    print("The Small Button is Pressed: " , SmallButtonPress.count)
SmallButtonPress.count = 0 
''' ======================================================= '''

''' To Display User Bill '''
def BillWindow():
	Bill_1 = Tk()
	Bill_1.geometry('300x100')
	Bill_1.title("------- [BILL] -------")

	''' Calculate User Bill '''
	T_Price =( (LargeButtonPress.count*10) + (MediumButtonPress.count*8) + (SmallButtonPress.count*5) )
	Bill_L = Label(Bill_1 , text="Total Price = {}".format(T_Price), bg='Black', fg = "#abd904", font = ("Times New Roman", 20) ).place(x=100 , y=40)

	Bill_1.mainloop ()
''' ======================================================= '''

''' ======================================================= '''
# pygame.mixer.init()
# def play ():
# 	pygame.mixer.music.load("Cane.mp3")
# 	pygame.mixer.music.play(loops = 0)
''' ======================================================= '''

window_1 = Tk ()
window_1.title ("ITI Sugar Cane Shop")
window_1.geometry ('800x700')

''' Background Photo '''
PH=Image.open(r"img\A.png")
PH=PH.resize((850 , 700))
PH=ImageTk.PhotoImage(PH)
''' ======================================================= '''

''' Close Program Button '''
L = Label(window_1, image = PH).place(x=-10 , y=0)
B = Button(window_1, text="X", bd='1', bg="red", command= window_1.destroy).place(x=0 , y=0)
''' ======================================================= '''

''' Welcome Label '''
LP = Label(window_1, text = "Welcome To ITI Sugar Cane Shop",bg='#b6c3b4', fg = "Black", font = ("Times New Roman", 30) ).pack(side = TOP , pady=50)
''' ======================================================= '''

''' Large Cup Photo & Configurations '''
PH1=Image.open(r"img\L.png")
PH1=PH1.resize((200, 200))
PH1=ImageTk.PhotoImage(PH1)
B1 = Button(window_1, text="Large Size", bd='3',activebackground= "#abd904", image=PH1, command=LargeButtonPress).place(x=50 , y=450)
L1 = Label(window_1, text = "Large = 10 EG",bg='Black', fg = "#abd904", font = ("Times New Roman", 15) ).place(x=90 , y=660)
''' ======================================================= '''

''' Medium Cup Photo & Configurations '''
PH2=Image.open(r"img\M.png")
PH2=PH2.resize((200, 200))
PH2=ImageTk.PhotoImage(PH2)
B2 = Button(window_1, text="Medium Size", bd='3', activebackground= "#abd904", image=PH2, command= MediumButtonPress).place(x=300 , y=450)
L2 = Label(window_1, text = "Medium = 8 EG",bg='Black', fg = "#abd904", font = ("Times New Roman", 15) ).place(x=340 , y=660)
''' ======================================================= '''

''' Small Cup Photo & Configurations '''
PH3=Image.open(r"img\S.png")
PH3=PH3.resize((200, 200))
PH3=ImageTk.PhotoImage(PH3)
B3 = Button(window_1, text="Small Size", bd='3',activebackground= "#abd904", image=PH3, command= SmallButtonPress).place(x=550 , y=450)
L3 = Label(window_1, text = "Small = 5 EG",bg='Black', fg = "#abd904", font = ("Times New Roman", 15) ).place(x=600 , y=660)
''' ======================================================= '''

''' Bill Photo & Configurations '''
PH4=Image.open(r"img\Bill.png")
PH4=PH4.resize((50, 30))
PH4=ImageTk.PhotoImage(PH4)
# B3 = Button(window_1, text="Small Size", bd='3',activebackground= "#abd904", image=PH3, command= SmallButtonPress).place(x=550 , y=450)
B4 = Button(window_1,text="BILL", bd='3', image=PH4,command=BillWindow).place(x=50,y=350)
L4 = Label(window_1, text="BILL", bg='Black', fg = "#abd904", font = ("Times New Roman", 15) ).place(x=55 , y=388)
''' ======================================================= '''


window_1.mainloop ()