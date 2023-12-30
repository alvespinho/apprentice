from tkinter import *
from tkinter import Tk
from tkinter import messagebox


## CORES ##
cor1 = "black"
cor2 = "white"
cor3 = "green"
cor4 = "value"
cor5 = "letter"

## CRIANDO JANELA ##
janela = Tk()
janela.title('Sistema de Login')
janela.geometry('310x300')
janela.config(bg = cor2)
janela.resizable(width=FALSE, height=FALSE)

## DIVIDINDO JANELA ##
frame_decima = Frame (janela, width= 310, height= 50, bg= cor2, relief='flat')
frame_decima.grid (row= 0, column= 0, pady= 1, padx= 0, sticky=NSEW)

frame_debaixo = Frame (janela, width= 310, height= 250, bg= cor2, relief='flat')
frame_debaixo.grid (row= 1, column= 0, pady= 1, padx= 0, sticky=NSEW)

## FRAME DE CIMA ##
login_nome = Label(frame_decima, text='LOGIN', anchor=NE, font =('Ivy 20'), bg=cor2, fg=cor1)
login_nome.place (x=5, y=5)


## SEPARADOR ##
separador = Label(frame_decima, text='', width=275, anchor= NW, font =('Ivy 1'), bg=cor3, fg=cor2)
separador.place (x=10, y=45)


credenciais = ['severo', '123456789']

# Função para Verificar Senha
def verifica_senha ():
    nome = campo_nome.get()
    senha = campo_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!')
    elif credenciais[0] == nome and credenciais [1] == senha: 
        messagebox.showinfo('Login', f'Seja bem vindo de volta, {credenciais[0]}!')

        for widget in frame_debaixo.winfo_children():
            widget.destroy()

        for widget in frame_decima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique nome e a senha.')

# Página após Verificação OK
def nova_janela():
## FRAME DE CIMA ##
    login_nome = Label(frame_decima, text=f'Usuário: {credenciais[0]}', anchor=NE, font =('Ivy 15'), bg=cor2, fg=cor1)
    login_nome.place (x=5, y=5)


    ## SEPARADOR ##
    separador = Label(frame_decima, text='', width=275, anchor= NW, font =('Ivy 1'), bg=cor3, fg=cor2)
    separador.place (x=10, y=45)

    login_nome = Label(frame_debaixo, text=f'Seja bem vindo, {credenciais[0]}', anchor=NE, font =('Ivy 15'), bg=cor2, fg=cor1)
    login_nome.place (x=5, y=105)


## FRAME DE BAIXO ##
label_nome = Label(frame_debaixo, text='Usuário: *', anchor=NW, font =('Ivy 10'), bg=cor2, fg=cor1)
label_nome.place (x=10, y=20)

campo_nome = Entry(frame_debaixo, text='', width=25, justify='left', font =('Ivy 10'), highlightthickness=1, relief='solid', bg=cor2, fg=cor1)
campo_nome.place (x=10, y=50)

label_pass = Label(frame_debaixo, text='Senha: *', anchor=NW, font =('Ivy 10'), bg=cor2, fg=cor1)
label_pass.place (x=10, y=100)

campo_pass = Entry(frame_debaixo, text='', width=25, justify='left', show='*', font =('Ivy 10'), highlightthickness=1, relief='solid', bg=cor2, fg=cor1)
campo_pass.place (x=10, y=130)

botao_entrar = Button(frame_debaixo, command=verifica_senha, text='Entrar', width=28, height= 1, justify='left', font =('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor2)
botao_entrar.place (x=10, y=170)

janela.mainloop()