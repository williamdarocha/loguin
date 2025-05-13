from tkinter import*
from PIL import Image, ImageTk

#cor
preto = "black"
branco = "white"
cinza = "#171616"
cinza_claro = "#1f1f1f"

#font
fonte = "Times 13 bold"

#configuração da janela
janela = Tk()
janela.resizable(height=False,width=False)
janela.geometry("550x400")
janela.config(bg=preto)
janela.title("Cavalo de Troia")

img = Image.open("ret.png")
icon = ImageTk.PhotoImage(img)
janela.call("wm","iconphoto",janela._w,icon)


def cadastro():
    #escondedo a tela de loguin
    e_nome.place(x=3000)
    e_senha.place(x=3000)
    b_loguin.place(x=3000)
    b_cadas.place(x=3000)
    #segunda telar
    nome["text"] = "Nome"

    e_nomecada = Entry(frame_dir,width=25,font=fonte)
    e_nomecada.place(x=10,y=50)

    senha["text"] = "Senha"
    senhacadas = Entry(frame_dir,width=25,font=fonte)
    senhacadas.place(x=10,y=130)

    l_email = Label(frame_dir,text="Email",font=fonte,bg=cinza,fg=branco)
    l_email.place(x=10,y=180)

    e_email = Entry(frame_dir,width=25,font=fonte)
    e_email.place(x=10,y=210)


    def vouta():
       #escondedo o formulario
       b_voutar.place(x=3000)
       b_inser.place(x=3000)
       e_email.place(x=3000)
       l_email.place(x=3000)
       e_nomecada.place(x=3000)
       senhacadas.place(x=3000)
       #mostrando a tela de loguin
       e_nome.place(x=10)
       e_senha.place(x=10)
       b_loguin.place(x=10)
       b_cadas.place(x=90)


    b_inser = Button(frame_dir,text="Inserir",font=fonte)
    b_inser.place(x=10,y=260)

    b_voutar = Button(frame_dir,command=vouta, text="Voltar", font=fonte)
    b_voutar.place(x=90, y=260)


#frame esquerdo
frame_esq = Frame(janela,width=270,height=400,bg=preto)
frame_esq.place(x=0,y=0)

#frame direito
frame_dir = Frame(janela,width=270,height=400,bg=cinza)
frame_dir.place(x=280,y=0)

#imagem
logo = PhotoImage(file="cavale.png")
logol = Label(frame_esq,image=logo,bg=preto)
logol.place(x=0,y=0)

#loguin
nome = Label(frame_dir,text="Nome",font=fonte,bg=cinza,fg=branco)
nome.place(x=10,y=20)

e_nome = Entry(frame_dir,width=15,font=fonte)
e_nome.place(x=10,y=50)

senha = Label(frame_dir,text="Senha",font=fonte,bg=cinza,fg=branco)
senha.place(x=10,y=100)

e_senha = Entry(frame_dir,width=15,font=fonte)
e_senha.place(x=10,y=130)

b_loguin = Button(frame_dir,text="loguin",font=fonte)
b_loguin.place(x=10,y=180)

b_cadas = Button(frame_dir,command=cadastro,text="cadastro",font=fonte)
b_cadas.place(x=90,y=180)

janela.mainloop()