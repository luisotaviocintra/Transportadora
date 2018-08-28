# -*- coding: iso-8859-1 -*-
import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Entry

# Criar conexÃ£o e cursor
con = sqlite3.connect('transportadora.db')
cur = con.cursor()



# Criar tabela clientes
cur.execute("""CREATE TABLE IF NOT EXISTS transportadora (
            tipoveiculo VARCHAR,
            modeloveiculo VARCHAR,
            pesoveiculo INTEGER,
            valorveiculo INTEGER)""")

class Navio:

    def __init__(self, master):

        # --------------------------------------TKINTER INTERFACE------------------------------------------------#
        self.frame1 = Frame(master, bg='sky blue')
        self.frame1.configure(relief=GROOVE)
        self.frame1.configure(borderwidth="2")
        self.frame1.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

        #--------------------------Titulo--------------------------#
        Label(self.frame1, text='Cadastrar Navio', font=('Ariel', '20'), bg='sky blue').place(relx=0.02, rely=0.01)

        # --------------------------Campo Entrada Nome--------------------------#
        self.txtNomenavio = StringVar()
        self.lblnomenavio = Label(master, text="Nome do Navio")
        self.lblnomenavio.place(relx=0.01, rely=0.10, relwidth=0.15)
        self.entNomenavio = Entry(master)
        self.entNomenavio.place(relx=0.17, rely=0.10)

        # --------------------------Campo Entrada Peso navio--------------------------#
        self.lblpesonavio = Label(master, text="Peso Suportado Pelo Navio")
        self.lblpesonavio.place(relx=0.01, rely=0.15, relwidth=0.25)
        self.entPesonavio = Entry(master)
        self.entPesonavio.place(relx=0.27, rely=0.15)

        # -- Botão Para inserir Navio -- "
        self.btnInserir = Button(master, text="Cadastrar Navio", command= self.cadastrarnavio)
        self.btnInserir.place(relx=0.01, rely=0.20, relheight=0.04, relwidth=0.15)


    def cadastrarnavio(self):
        nomedonavio1 = self.entNomenavio.get()
        pesonavio1 = self.entPesonavio.get()
        if int(pesonavio1) <= 0:
            messagebox.showinfo('Aviso!', 'Por favor coloque o Peso suportado pelo Navio')
            self.entPesonavio.delete(0, END)
        else:
            messagebox.showinfo('Aviso!', 'Navio Cadastrado com Sucesso')

            # --------------------------------------TKINTER INTERFACE------------------------------------------------#
            self.frame1 = Frame(bg='sky blue')
            self.frame1.configure(relief=GROOVE)
            self.frame1.configure(borderwidth="2")
            self.frame1.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

            # --------------------------Titulo--------------------------#
            Label(self.frame1, text='Cadastrar Veiculo', font=('Ariel', '20'), bg='sky blue').place(relx=0.02,
                                                                                                    rely=0.02)

            # -- Cadastrar Tipo Veiculos -- "
            self.tipoveiculo = tkinter.StringVar()
            self.tipoveiculo.set('Tipo Veiculo')
            self.TipoVeiculo = ttk.Combobox(textvariable=self.tipoveiculo)
            self.TipoVeiculo.place(relx=0.01, rely=0.10, relheight=0.04, relwidth=0.15)
            self.TipoVeiculo['values'] = ('Bicicleta', 'Moto', 'Carro', 'Caminhão', 'Avião')

            # -- Cadastrar Modelo Veiculos -- "
            self.modeloveiculo = tkinter.StringVar()
            self.modeloveiculo.set('Modelo Veiculo')
            self.ModeloVeiculo = ttk.Combobox(textvariable=self.modeloveiculo)
            self.ModeloVeiculo.place(relx=0.17, rely=0.10, relheight=0.04, relwidth=0.15)
            self.ModeloVeiculo['values'] = ('SCOOT', 'SPECIALIZED', 'GIANT', 'DUCATI', 'HONDA', 'BWM', 'MERCEDES',
                                            'AUDI', 'FIAT', 'SCANIA', 'VOLVO', 'IVECO', 'AIRBUS', 'EMBAER', 'BOEING')

            # -- Cadastrar Peso do Veiculo -- "
            self.pesoveiculo = tkinter.IntVar()
            self.pesoveiculo.set('Peso Veiculo')
            self.PesoVeiculo = ttk.Combobox(textvariable=self.pesoveiculo)
            self.PesoVeiculo.place(relx=0.33, rely=0.10, relheight=0.04, relwidth=0.13)

            # -- Cadastrar Valor do Veiculo -- "
            self.valorveiculo = tkinter.StringVar()
            self.valorveiculo.set('Valor Veiculo')
            self.ValorVeiculo = ttk.Combobox(textvariable=self.valorveiculo)
            self.ValorVeiculo.place(relx=0.47, rely=0.10, relheight=0.04, relwidth=0.13)

            # -- Botão Para Inserir Veiculo -- "
            self.btnInserirveiculo = Button(text="Cadastrar Veiculo", command=self.cadastrarveiculo)
            self.btnInserirveiculo.place(relx=0.63, rely=0.10, relheight=0.04, relwidth=0.15)

            # --------------------------Fundo Campo de entrega--------------------------#
            self.frame2 = Frame()
            self.frame2.configure(relief=GROOVE)
            self.frame2.configure(borderwidth="2")
            self.frame2.place(relx=0.01, rely=0.17, relheight=0.59, relwidth=0.98)
            self.mostra1 = Text(self.frame2, bg='azure', fg='black')
            self.mostra1.place(relx=0.00, rely=0.0, relheight=1.0, relwidth=1.0)

            # --------- Tela Para Mostrar Peso Suportado pelo navio ---------#
            self.mostra2 = Text(self.frame1, bg='sky blue', fg='black')
            self.mostra2.place(relx=0.55, rely=0.78, relheight=0.04, relwidth=0.10)
            Label(self.frame1, text='Peso Suportado pelo Navio: ', font=('Ariel', '10'), bg='sky blue').place(relx=0.30, rely=0.78)

            #--------- Tela Para Mostrar Peso Total Dos Veiculos ---------#
            self.mostra3 = Text(self.frame1, bg='sky blue', fg='black')
            self.mostra3.place(relx=0.89, rely=0.78, relheight=0.04, relwidth=0.10)
            Label(self.frame1, text='Peso Total dos veiculos: ', font=('Ariel', '10'), bg='sky blue').place(relx=0.67, rely=0.78)

            # --------- Tela Para Mostrar Quantidade de Veiculos ---------#
            self.mostra4 = Text(self.frame1, bg='sky blue', fg='black')
            self.mostra4.place(relx=0.11, rely=0.78, relheight=0.04, relwidth=0.10)
            Label(self.frame1, text='Veiculos: ', font=('Ariel', '10'), bg='sky blue').place(relx=0.01, rely=0.78)

    #-- Cadastrando o veiculo --#
    def cadastrarveiculo(self):

        #-- Pegando as variaveis --#
        pesonavio2 = int(self.entPesonavio.get())
        tipoveiculo1 = self.tipoveiculo.get()
        modeloveiculo1 = self.modeloveiculo.get()
        pesoveiculo1 = int(self.pesoveiculo.get())
        valorveiculo1 = int(self.valorveiculo.get())

        #-- Inserindo o Veiculo no banco de dados --#
        if pesoveiculo1 >= pesonavio2:
            messagebox.showinfo('Aviso!', 'Veiculo Muito pesado, o Navio não suporta.')
        else:
            try:
                cur.execute("INSERT INTO transportadora VALUES(?,?,?,?)", (tipoveiculo1, modeloveiculo1, pesoveiculo1, valorveiculo1))
            except:
                messagebox.showinfo('Aviso!', 'Modelo já cadastrado.')
            con.commit()

            #-- Listando os veiculos na tela --#
            cur.execute("SELECT * FROM transportadora")
            consulta = cur.fetchall()
            self.mostra1.delete(0.0, END)
            for i in consulta:
                self.mostra1.insert(END, "Tipo: {} | Modelo: {} | Peso: {} | Valor: {} |\n" .format(i[0], i[1], i[2], i[3]))

            #-- Informando peso suportado pelo navio --#
            self.mostra2.delete(0.0, END)
            self.mostra2.insert(END, "{}" .format(int(pesonavio2)))

            #-- Somando o peso dos veiculos na tela --#
            cur.execute("SELECT SUM (pesoveiculo) FROM transportadora")
            consulta = cur.fetchall()
            for i in consulta:
                self.mostra3.delete(0.0, END)
                self.mostra3.insert(END, "{} \n" .format(i[0]))

            # -- Somando Quantidade de veiculos --#
            cur.execute("SELECT COUNT (tipoveiculo) FROM transportadora")
            consulta = cur.fetchall()
            for i in consulta:
                self.mostra4.delete(0.0, END)
                self.mostra4.insert(END, "{} \n".format(i[0]))
            #-- Limpando as informações dos campos --#
            self.TipoVeiculo.delete(0, END)
            self.ModeloVeiculo.delete(0, END)
            self.PesoVeiculo.delete(0, END)
            self.ValorVeiculo.delete(0, END)







root = Tk()
root.title("Transportadora")
root.geometry("700x600")
Navio(root)
root.mainloop()