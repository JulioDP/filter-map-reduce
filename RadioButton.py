import tkinter
from tkinter import ttk

window =  tkinter.Tk()
window.configure(bg='black')

window.columnconfigure(0, weight=1)
window.columnconfigure(1,weight=3)



lista_label = ttk.Label(window, text='Tipo vehiculo')
lista_label.grid(column=1, row=0, padx=20, pady=10 )

seleccionado = tkinter.StringVar()
radiobtn1 = ttk.Radiobutton(window, text='Avion', value='1', variable=seleccionado)
radiobtn1.grid(column=1, row=1, padx=10, pady=10)

radiobtn2 = ttk.Radiobutton(window, text='Moto', value='2', variable=seleccionado)
radiobtn2.grid(column=1, row=2, padx=10, pady=10)

radiobtn3 = ttk.Radiobutton(window, text='carro', value='3', variable=seleccionado)
radiobtn3.grid(column=1, row=3, padx=10, pady=10)

radiobtn3 = ttk.Radiobutton(window, text='bicicleta', value='4', variable=seleccionado)
radiobtn3.grid(column=1, row=4, padx=10, pady=10)

def reiniciar(event):
    seleccionado.set(0)
reincio_btn = ttk.Button(text='Reinicio')
reincio_btn.grid(column=1, row=5)
reincio_btn.bind('<Button-1>',reiniciar)

window.mainloop()