import tkinter as tk
import pyperclip
from tkinter import messagebox

class MyApplication:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Gerenciador de contas")
        
        #criar uma lista de contas
        self.contas_principal=tk.Listbox(self.window,height=10,width=100,font=("Arial",12))
        self.contas_principal.grid(row=0,column=0,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        #carregar as contas na lista
        self.carregar_contas()
        
        
        #adiciona um quadro para colocar os botões e em seguida adiciona ao grid        
        button_frame_principal=tk.Frame(self.window)
        
        py=40
        tk.Button(button_frame_principal,text="Copiar Email",command=self.copiar_email_principal).pack(padx=10,pady=py,side="top")
        tk.Button(button_frame_principal,text="Copiar Senha",command=self.copiar_senha_principal).pack(padx=10,pady=(0,py),side="top")
        
        button_frame_principal.grid(row=0,column=2,sticky="nsew")
        
        #criando frame de pesquisa com base no email
        email_frame=tk.Frame(self.window)
        
        tk.Label(email_frame,text="Digite o email para pesquisar").pack(pady=5)
        self.email_entry=tk.Entry(email_frame,width=30)
        self.email_entry.pack(pady=5)
        tk.Button(email_frame,text="Procurar por email",command=self.procura_email).pack(pady=5)
        
        email_frame.grid(row=1,column=0,sticky="nsew")
        
        #criando frame de pesquisa com base no nome do site
        nome_frame=tk.Frame(self.window)
        
        tk.Label(nome_frame,text="Digite o nome do site para pesquisar").pack(pady=5)
        self.nome_entry=tk.Entry(nome_frame,width=30)
        self.nome_entry.pack(pady=5)
        tk.Button(nome_frame,text="Procurar por nome",command=self.procura_nome_site).pack(pady=5)
        
        nome_frame.grid(row=1,column=1,sticky="nsew")
        
        #criando a lista que vai armazenar as contas que vão ser buscadas tanto por email quanto por nome
        self.contas_procura=tk.Listbox(self.window,height=10,width=100)
        self.contas_procura.grid(row=2,column=0,columnspan=2,sticky="nsew",padx=5,pady=5)
        
        button_frame_procura=tk.Frame(self.window)
        
        py=20
        tk.Button(button_frame_procura,text="Copiar Email",command=self.copiar_email_procura).pack(padx=10,pady=py,side="top")
        tk.Button(button_frame_procura,text="Copiar Senha",command=self.copiar_senha_procura).pack(padx=10,pady=(0,py),side="top")
        
        button_frame_procura.grid(row=2,column=2,sticky="nsew")
        
           
        self.window.mainloop()
        
    def carregar_contas(self):
        try:
            with open("contas.txt","r",encoding="utf-8") as f:
                for line in f:
                    email,senha,nome_site=line.strip().split(";")
                    self.adicionar_contas_lista(email,senha,nome_site)
        except FileNotFoundError:
            with open("contas.txt","w") as f:
                pass
                    
    def adicionar_contas_lista(self,email,senha,nome_site):
        self.contas_principal.insert(tk.END,f"{email} - {senha} - {nome_site}")
        
    def adicionar_contas_lista_procura(self,lista):
        self.contas_procura.delete("0","end")
        for l in lista:
            self.contas_procura.insert(tk.END,f"{l[0]} - {l[1]} - {l[2]}")
        
        
    def procura_email(self):
        email=self.email_entry.get().strip()
        if len(email)>0:
            lista_procura_email=[]
            lista_principal=self.contas_principal
            for i in range(lista_principal.size()):
                if email.lower() in lista_principal.get(i).split("-")[0].strip().lower():
                    lista_procura_email.append(lista_principal.get(i).split("-"))
                else:
                    pass
            self.adicionar_contas_lista_procura(lista_procura_email)
        else:    
            pass
    
    def procura_nome_site(self):
        nome_site=self.nome_entry.get().strip()
        if len(nome_site)>0:
            lista_procura_nome_site=[]
            lista_principal=self.contas_principal
            for i in range(lista_principal.size()):
                if nome_site.lower() in lista_principal.get(i).split("-")[2].strip().lower():
                    lista_procura_nome_site.append(lista_principal.get(i).split("-"))
                else:
                    pass
            self.adicionar_contas_lista_procura(lista_procura_nome_site)
        else:    
            pass
        
    #abaixo são as funções dos botões para copiar email ou senha
    def copiar_email_principal(self):
        is_selecionada=self.contas_principal.curselection()
        
        if is_selecionada:
            linha_selecionada=self.contas_principal.get(is_selecionada[0])
            email_selecionado=linha_selecionada.split("-")[0].strip()
            pyperclip.copy(email_selecionado)
        else:
            messagebox.showerror("Erro", "Nenhuma linha selecionada")
            
    def copiar_senha_principal(self):
        is_selecionada=self.contas_principal.curselection()
        
        if is_selecionada:
            linha_selecionada=self.contas_principal.get(is_selecionada[0])
            senha_selecionada=linha_selecionada.split("-")[1].strip()
            pyperclip.copy(senha_selecionada)
        else:
            messagebox.showerror("Erro", "Nenhuma linha selecionada")
            
    def copiar_email_procura(self):
        is_selecionada=self.contas_procura.curselection()
        
        if is_selecionada:
            linha_selecionada=self.contas_procura.get(is_selecionada[0])
            email_selecionado=linha_selecionada.split("-")[0].strip()
            pyperclip.copy(email_selecionado)
        else:
            messagebox.showerror("Erro", "Nenhuma linha selecionada")
            
    def copiar_senha_procura(self):
        is_selecionada=self.contas_procura.curselection()
        
        if is_selecionada:
            linha_selecionada=self.contas_procura.get(is_selecionada[0])
            senha_selecionada=linha_selecionada.split("-")[1].strip()
            pyperclip.copy(senha_selecionada)
        else:
            messagebox.showerror("Erro", "Nenhuma linha selecionada")
            
    
            
        
    
        
    
app=MyApplication()