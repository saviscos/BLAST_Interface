#!/usr/bin/env
from tkinter import *
#import posiciona
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

#definindo blast
BLAST="/path/to/ncbi-blast-2.2.26+/bin"

global en_database
global en_entradaBlast
global en_tipoDeBlast
global en_evalue
global en_tipoDeDatabase

# Funções
def buscadb():
    global en_database
    en_database = filedialog.askopenfilename(initialdir="/",
                                          title="Procure o Banco de Dados",
                                          filetypes=(("Arquivo em Fasta",
                                                      "*.f*"),
                                                     ("Todos arquivos",
                                                      "*.*")))
    bt_escolherdb.configure(text= en_database.split('/')[-1], font=('Helvatical bold',12))


def buscaquery():
    global en_entradaBlast
    en_entradaBlast = filedialog.askopenfilename(initialdir="/",
                                          title="Procure o arquivo alvo",
                                          filetypes=(("Arquivo em Fasta",
                                                      "*.f*"),
                                                     ("Todos arquivos",
                                                      "*.*")))
    bt_escolherquery.configure(text= en_entradaBlast.split('/')[-1], font=('Helvatical bold',12))


def makedb():
    global en_database
    bancodedados = en_tipoDeDatabase.get()
#    messagebox.showinfo("Formatando o Banco de Dados", "FAZENDO BANCO DE DADOS PARA  " + database)
    os.system('makeblastdb -in ' + en_database + ' -dbtype ' + bancodedados)
    messagebox.showinfo("Fazendo banco de dados","SEU BANCO DE DADOS FOI FORMATADO!")


def blastando():
    global en_database
    global en_entradaBlast
    global en_tipoDeBlast
    blasttype = en_tipoDeBlast.get()
    value = en_evalue.get()     
    os.system(blasttype + ' -query ' + en_entradaBlast + ' -db ' + en_database + ' -evalue ' + value + ' -outfmt 7' + ' -out arquivoDeSaida')
 #   os.system(blasttype + ' -evalue ' + evaluevalor + ' -outfmt 6 ' + ' -query ' + en_entradaBlast + ' -db ' + en_database + ' -out ./saidablast')
 #   messagebox.showinfo("Fazendo alinhamento", "FAZENDO BLAST DO  " + database + "\s" + entradablast)
    messagebox.showinfo("Blastando", "Seu BLAST terminou!")

master = Tk()
master.title("Alinhamento com BLAST")
master.geometry("490x560+610+153")
master.resizable(width=False, height=False)

#usando o posiciona
#master.bind('<Button-1>', posiciona.inicio_place)
#master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master))
#master.bind('<Button-2>', lambda arg: posiciona.para_geometry(master))

# Importar imagens Linux
#img_fundo = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/Fundo.png")
#img_botao1 = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/DB.png")
#img_botao2 = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/BLASTAR.png")

# Importar imagens windows
img_fundo = PhotoImage(file="imagens\\Fundo.png")
img_botao1 = PhotoImage(file="imagens\\DB.png")
img_botao2 = PhotoImage(file="imagens\\BLASTAR.png")

# Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

# Criação de caixas de entrada
#en_database = filedialog.askopenfilename(initialdir = "/",title = "Selecione o arquivo",
#                                          filetypes = (("fasta files",
#                                                        "*.f*"),
#                                                       ("all files",
#                                                        "*.*")))
#en_database = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
#en_database.place(width=259, height=42, x=113, y=195)

#en_entradaBlast = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
#en_entradaBlast.place(width=273, height=45, x=92, y=347)

#entradaComOpção
en_tipoDeDatabase = ttk.Combobox(master,values=["nucl","prot"])
en_tipoDeDatabase.place(width=117, height=37, x=315, y=177)

en_tipoDeBlast = ttk.Combobox(master,values=["blastn","blastp","blastx"])
en_tipoDeBlast.place(width=122, height=35, x=40, y=430)

#Entrada escrita
en_evalue = Entry(master, bd=2, font=("Calibri", 13), justify=CENTER)
en_evalue.place(width=110, height=28, x=323, y=423)

# Criação de botões
bt_escolherdb = Button(master, text= "Escolha o Banco de Dados", command=buscadb)
bt_escolherdb.place(width=220, height=36, x=35, y=178)

bt_fazerBanco = Button(master, bd=0, image=img_botao1, command=makedb)
bt_fazerBanco.place(width=166, height=45, x=164, y=247)

bt_blastar = Button(master, bd=0, image=img_botao2, command=blastando)
bt_blastar.place(width=173, height=63, x=162, y=487)

bt_escolherquery = Button(master, text= "Procure o arquivo alvo", command=buscaquery)
bt_escolherquery.place(width=215, height=48, x=147, y=328)

master.mainloop()

