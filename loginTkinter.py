# Importando o Tkinter e seu widget Messagebox
import tkinter as tk
from tkinter import messagebox

# Criando Cores
cor_gelo_derretido = '#fcfafa'
cor_amarelo_burro = '#bfbd36'

root = tk.Tk()
root.title('Login')
root.geometry('150x200')
root.config(bg=cor_gelo_derretido)

# Criando a Função
def validar_usuario():
    email = entry_email.get()
    senha = entry_senha.get()
    if '@' not in email:
        messagebox.showerror('Erro', 'E-mail está errado!')
    elif len(senha) < 7:
        messagebox.showerror('Erro', 'Senha está errada!')
    else:
        messagebox.showinfo('Confirmado','Login realizado com sucesso!') 
    
# Criando Widgets
label_email = tk.Label(root, text='Insira seu e-mail', font=('Arial', 10), bg=cor_gelo_derretido)
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=0, padx=10, pady=5)

label_senha = tk.Label(root, text='Insira sua senha', font=('Arial', 10), bg=cor_gelo_derretido)
label_senha.grid(row=3, column=0, padx=10, pady=5)
entry_senha = tk.Entry(root, show='*') # Uso do widget Show para esconder a senha digitada
entry_senha.grid(row=2, column=0, padx=10, pady=5)

# Criando o Button
botao_entrar = tk.Button(root, text='Entrar', font=('Arial', 10), bg=cor_amarelo_burro, command=validar_usuario)
botao_entrar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()