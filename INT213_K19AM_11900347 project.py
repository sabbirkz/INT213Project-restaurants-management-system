from tkinter import *

root = Tk()
root.geometry("900x600+300+100")
root.title("INT213 Project by Kazi Zafar Ahmmed Sabbir")

#--------------Header---------

topbar = Label(root, text="Restaurants Management System", bg="red", font=('arial', 30, 'bold'))
topbar.pack(fill=X)
topbar2 = Label(root, text="Submitted By :- Kazi Zafar Ahmmed Sabbir (11900347)", bg="red", font=('arial', 10, 'bold'))
topbar2.pack(fill=X)

#-------------Header---------


#---------Body-------------
frame = LabelFrame(root, text="Place Your Order", labelanchor="n", padx=300, pady=50, font=('arial', 17, 'bold') )

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

c1 = Checkbutton(frame, text='Rice',variable=var1, font=('arial', 15, 'bold'))
c1.pack()
c2 = Checkbutton(frame, text='Vegetable', variable=var2,font=('arial', 15, 'bold'))
c2.pack()
c3 = Checkbutton(frame, text='Set Menu', variable=var3, font=('arial', 15, 'bold'))
c3.pack()
c4 = Checkbutton(frame, text='Salad',variable=var4, font=('arial', 15, 'bold'))
c4.pack()
c5 = Checkbutton(frame, text='Soft Drinks', variable=var5, font=('arial', 15, 'bold'))
c5.pack()
c6 = Checkbutton(frame, text='Mineral water', variable=var6, font=('arial', 15, 'bold'))
c6.pack()

button1 = Button(frame, text="Coupon Code", padx=2, pady=2, bg='cyan')
button1.pack(side=LEFT, pady=20)
button2 = Button(frame, text="Place Order", padx=2, pady=2, bg='cyan')
button2.pack(side=LEFT)
button3 = Button(frame, text="Feedback", padx=2, pady=2, bg='cyan')
button3.pack(side=LEFT)

frame.pack()

#--------- Body -------------


# ------ Footer ------
bottomFrame = Frame(root)

footer = Label(bottomFrame, text="-----: Thank You for Visiting Us :-----", bg="red", font=('arial', 10, 'bold'))
footer.pack()

bottomFrame.pack(side=BOTTOM)

# --- Footer ------
root.mainloop()
