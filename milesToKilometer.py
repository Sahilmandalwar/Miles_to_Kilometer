from tkinter import *

FONT = ("Arial",12,"bold")
window = Tk()
window.minsize(height=100,width=200)

window.config(padx=35,pady=35)
window.title("Mile to Km Converter")
window["bg"] = "white"

#entry
entry = Entry(width = 15)
entry.insert(END,string="0")
entry.grid(row=0,column=1)

#label-1
label_1 = Label(text="is equal to",font=FONT,bg="white",padx=5,pady=5)
label_1.grid(row=1,column=0)

#label-2
label_2 = Label(text="0",font=FONT,bg="white",padx=5,pady=5)
label_2.grid(row=1,column=1)

#label-3
label_3 = Label(text="Miles",font=FONT,bg="white",padx=5,pady=5)
label_3.grid(row=0,column=2)

#label_4
label_4 = Label(text="Km",font=FONT,bg="white",padx=5,pady=5)
label_4.grid(row=1,column=2)

#button
def calculate_Km():
    inMiles = entry.get()
    inKm = float(inMiles) * 1.609344
   
    label_2.config(text="{:.2f}".format(inKm))

button = Button(text="Calculate",font=FONT,command=calculate_Km,bg="red",fg="white",padx=5,pady=5)
button.grid(row=2,column=1)




window.mainloop()