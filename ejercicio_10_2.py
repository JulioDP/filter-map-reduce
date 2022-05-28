import tkinter
from tkinter import ttk
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista_label = ttk.Label(window,text='Elige las opciones')
lista_label.grid(column=0, row=0)

lista_label1 = ttk.Label(window,text='Examen')
lista_label1.grid(column=0, row=1)
select1 = tkinter.BooleanVar()
check1 = ttk.Checkbutton(window, variable=select1, onvalue=True, offvalue=False )
check1.grid(column=1, row=1)

lista_label2 = ttk.Label(window,text='Proyecto')
lista_label2.grid(column=0, row=2)

select2 = tkinter.BooleanVar()
check2 = ttk.Checkbutton(window, variable=select2, onvalue=True, offvalue=False)
check2.grid(column=1, row=2)

lista_label3 = ttk.Label(window,text='Diplomado')
lista_label3.grid(column=0, row=3)

select3 = tkinter.BooleanVar()
check3 = ttk.Checkbutton(window, variable=select3, onvalue=True, offvalue=False)
check3.grid(column=1, row=3)

def listar():
    if select1.get() == True:
        print('Examen')
    if select2.get() == True:
        print('Proyecto')
    if select3.get() == True:
        print('Diplomado')

btn_lista = ttk.Button(window, text='Listar', command=listar)
btn_lista.grid(column=1, row=4)

window.mainloop()
