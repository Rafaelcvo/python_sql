from tkinter import *
from tkinter import messagebox
from tkinter import ttk


jan = Tk()
jan.title("Acess Painel")
jan.geometry("600x300")
jan.config(background="white")
jan.resizable(width=False, height=False)

nome = Label(text="Nome:", fg="Black")
nome.place(x=20, y=10)
nomeEntry = ttk.Entry(width=60)
nomeEntry.place(x=100, y=10)

endereco = Label(text="Endereço:", fg="black")
endereco.place(x=20, y=40)
enderecoEntry = ttk.Entry(width=60)
enderecoEntry.place(x=100, y=40)


jan.mainloop()