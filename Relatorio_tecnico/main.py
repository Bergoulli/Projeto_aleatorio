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
        Dataframe.place(x=0,y=100, width=1440, height=550)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Dados do cliente: ')
        Dataframeleft.place(x=0,y=5, width=930, height=150)

        Dataframedown = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Informações da Inspeção: ')
        Dataframedown.place(x=0,y=170, width=930, height=120)

        Dataframeinpe = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Informações da Inspeção: ')
        Dataframeinpe.place(x=0,y=300, width=930, height=220)

        Dataframeright= LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('times new roman', 12, 'bold'), text='Descrição: ')
        Dataframeright.place(x=940,y=5, width=460, height=350)
        
        #=================buttons frame============

        Buttonframe = Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=660, width=1440, height=60)

        #======================buttons ====================

        btnpdf=Button(Buttonframe, text='PDF', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btnpdf.grid(row=0, column=0)

        btnsair=Button(Buttonframe, text='Sair', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btnsair.grid(row=0, column=1)

        btndescri=Button(Buttonframe, text='Descrição', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btndescri.grid(row=0, column=2)

        btndescri=Button(Buttonframe, text='Data de Descrip.', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btndescri.grid(row=0, column=3)

        btndelete=Button(Buttonframe, text='Deletar', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btndelete.grid(row=0, column=4)

        btnlimpar=Button(Buttonframe, text='Limpar', bg='green', fg='white', font=('times new roman',12, 'bold'), width=23, height=1, padx=2, pady=2)
        btnlimpar.grid(row=0, column=5)

        #=================details============

        Detailsframe = Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=720, width=1440, height=120)

        #dataframe left - cliente ================================

        self.txtdescription = Text(Dataframeright, font=('times new roman',12), width=52, height=16, padx=2, pady=6)
        self.txtdescription.grid(row=0, column=0)



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

        Lbltipoclient=Label(Dataframeleft, font=('times new roman',12, 'bold'), text='Nome/empresa', padx=2, pady=6)
        Lbltipoclient.grid(row=2, column=7, sticky=W)
        texttipoclient=Entry(Dataframeleft, font=('times new roman',12), width=35)
        texttipoclient.grid(row=2, column=8)

        #dataframe down - responsável ================================

        Lblprojectclient=Label(Dataframedown, font=('times new roman',12, 'bold'), text='Nome do projeto', padx=2, pady=6)
        Lblprojectclient.grid(row=0, column=0, sticky=W)
        textprojectclient=Entry(Dataframedown, font=('times new roman',12), width=35)
        textprojectclient.grid(row=0, column=1)

        Lbldataclient=Label(Dataframedown, font=('times new roman',12, 'bold'), text='Data/hora', padx=2, pady=6)
        Lbldataclient.grid(row=0, column=7, sticky=W)
        textdataclient=Entry(Dataframedown, font=('times new roman',12), width=35)
        textdataclient.grid(row=0, column=8)

        Lblrespclient=Label(Dataframedown, font=('times new roman',12, 'bold'), text='Responsável', padx=2, pady=6)
        Lblrespclient.grid(row=1, column=0, sticky=W)
        textrespclient=Entry(Dataframedown, font=('times new roman',12), width=35)
        textrespclient.grid(row=1, column=1)

        #dataframe inspe - inspeção ================================

        lblNametablet = Label(Dataframeinpe, text='Estado da estrutura', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblNametablet.grid(row=0, column=0)
        comNametablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comNametablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comNametablet.grid(row=0, column=1)

        lbllimpetablet = Label(Dataframeinpe, text='Limpeza', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lbllimpetablet.grid(row=1, column=0)
        comlimpetablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comlimpetablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comlimpetablet.grid(row=1, column=1)

        lblinstaltablet = Label(Dataframeinpe, text='Inst. Elétrica', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblinstaltablet.grid(row=2, column=0)
        cominstaltablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        cominstaltablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        cominstaltablet.grid(row=2, column=1)

        lbldocumentablet = Label(Dataframeinpe, text='Documentação', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lbldocumentablet.grid(row=3, column=0)
        comdocumentablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comdocumentablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comdocumentablet.grid(row=3, column=1)

        lblepitablet = Label(Dataframeinpe, text='EPIs', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblepitablet.grid(row=4, column=0)
        comepitablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comepitablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comepitablet.grid(row=4, column=1)

        lblidenttablet = Label(Dataframeinpe, text='Ident. funcion.', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblidenttablet.grid(row=0, column=3)
        comidenttablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comidenttablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comidenttablet.grid(row=0, column=4)

        lblisolatablet = Label(Dataframeinpe, text='Isolação', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblisolatablet.grid(row=1, column=3)
        comisolatablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comisolatablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comisolatablet.grid(row=1, column=4)

        lblconectablet = Label(Dataframeinpe, text='Conexões', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblconectablet.grid(row=2, column=3)
        comconectablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comconectablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comconectablet.grid(row=2, column=4)

        lbldisjunttablet = Label(Dataframeinpe, text='Disjuntores', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lbldisjunttablet.grid(row=3, column=3)
        comdisjunttablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comdisjunttablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comdisjunttablet.grid(row=3, column=4)

        lblaterratablet = Label(Dataframeinpe, text='Aterramento', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblaterratablet.grid(row=4, column=3)
        comaterratablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comaterratablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comaterratablet.grid(row=4, column=4)

        lblequipablet = Label(Dataframeinpe, text='Equipamentos', font=('times new roman',12, 'bold'), padx=2, pady=6)
        lblequipablet.grid(row=0, column=6)
        comequipablet = ttk.Combobox(Dataframeinpe, font=('times new roman',12), width=13)
        comequipablet['values'] = ('Conforme', 'Não conforme', 'N/A')
        comequipablet.grid(row=0, column=7)


        #==================tabela=================================


        #=====================scrol======================
        scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.relatorio_table = ttk.Treeview(Detailsframe, columns=('Nomeprojeto', 'Responsavel', 'Cliente', 'Email', 'Telefone', 'Data'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.relatorio_table.xview)
        scroll_y=ttk.Scrollbar(command=self.relatorio_table.yview)

        self.relatorio_table.heading('Nomeprojeto', text='Nome do projeto')
        self.relatorio_table.heading('Responsavel', text='Responsável')
        self.relatorio_table.heading('Cliente', text='Cliente')
        self.relatorio_table.heading('Email', text='E-mail')
        self.relatorio_table.heading('Telefone', text='Telefone')
        self.relatorio_table.heading('Data', text='Data')

        self.relatorio_table['show']='headings'
        self.relatorio_table.pack(fill=BOTH, expand=1)

root = Tk()
ob = Relatorio(root)
root.mainloop()