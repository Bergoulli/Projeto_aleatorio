from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Relatorio:
    def __init__(self, root):
        self.root=root
        self.root.title('Relatório de Instalações')
        self.root.geometry('1440x850+0+0')

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text='RELATÓRIO DE INSTALAÇÕES', fg='red', bg='white', font=('times new roman', 30, 'bold'))
        lbltitle.pack(side=TOP, fill=X)


        #"============dataframe============"
        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=130, width=1440, height=550)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Dados do cliente: ')
        Dataframeleft.place(x=0,y=5, width=930, height=250)
        Dataframedown = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Informações da Inspeção: ')
        Dataframedown.place(x=0,y=270, width=930, height=250)

        Dataframeright= LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Descrição: ')
        Dataframeright.place(x=940,y=5, width=460, height=350)
        
        #=================buttons frame============

        Buttonframe = Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=690, width=1440, height=70)

        
        #=================details============

        Detailsframe = Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=770, width=1440, height=70)

        #dataframe left - cliente ================================

        Lblnameclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='Cliente', padx=2, pady=6)
        Lblnameclient.grid(row=0, column=0, sticky=W)
        textnameclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        textnameclient.grid(row=0, column=1)

        Lblcnpgclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='CNPJ/CPF', padx=2, pady=6)
        Lblcnpgclient.grid(row=0, column=7, sticky=W)
        textcnpgclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        textcnpgclient.grid(row=0, column=8)

        Lblenderecoclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='Endereço', padx=2, pady=6)
        Lblenderecoclient.grid(row=1, column=0, sticky=W)
        textenderecoclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        textenderecoclient.grid(row=1, column=1)

        Lbltelefclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='Número de telefone', padx=2, pady=6)
        Lbltelefclient.grid(row=1, column=7, sticky=W)
        texttelefclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        texttelefclient.grid(row=1, column=8)

        Lblemailclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='E-mail', padx=2, pady=6)
        Lblemailclient.grid(row=2, column=0, sticky=W)
        textemailclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        textemailclient.grid(row=2, column=1)

        #dataframe left - responsável ================================

        # lblNametablet = Label(Dataframeleft, text='teste', font=('times new roman',12, 'bold'), padx=2, pady=6)
        # lblNametablet.grid(row=1, column=0)

        # comNametablet = ttk.Combobox(Dataframeleft, font=('times new roman',12),
        #                              width=33)
        # comNametablet.grid(row=1, column=1)


root = Tk()
ob = Relatorio(root)
root.mainloop()