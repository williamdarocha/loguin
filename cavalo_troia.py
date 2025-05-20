from tkinter import*
from tkinter import messagebox
import banco
#from PIL import Image, ImageTk

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

#img = Image.open("ret.png")
#icon = ImageTk.PhotoImage(img)
#janela.call("wm","iconphoto",janela._w,icon)


def cadastro():
    #escondedo a tela de loguin
    e_nome.place(x=3000)
    e_senha.place(x=3000)
    b_loguin.place(x=3000)
    b_cadas.place(x=3000)
    listabox.place(x=3000)
    b_lista.place(x=3000)
    #segunda telar
    nome["text"] = "Nome"
    nome.place(y=20)

    e_nomecada = Entry(frame_dir,width=25,font=fonte)
    e_nomecada.place(x=10,y=50)

    l_usuario = Label(frame_dir,text="Usuario",font=fonte,bg=cinza,fg=branco)
    l_usuario.place(x=10,y=100)

    e_usuario = Entry(frame_dir,width=25,font=fonte)
    e_usuario.place(x=10,y=130)

    senha["text"] = "Senha"
    senha.place(y=180)
    senhacadas = Entry(frame_dir,width=25,font=fonte)
    senhacadas.place(x=10,y=210)

    l_email = Label(frame_dir,text="Email",font=fonte,bg=cinza,fg=branco)
    l_email.place(x=10,y=260)

    e_email = Entry(frame_dir,width=25,font=fonte)
    e_email.place(x=10,y=290)


    def vouta():
       #escondedo o formulario
       b_voutar.place(x=3000)
       b_inser.place(x=3000)
       e_email.place(x=3000)
       l_email.place(x=3000)
       e_nomecada.place(x=3000)
       senhacadas.place(x=3000)
       e_usuario.place(x=3000)
       l_usuario.place(x=3000)
       #mostrando a tela de loguin
       listabox.place(x=5,y=6)
       nome.place(x=10,y=130)
       senha.place(x=10,y=210)
       e_nome.place(x=10,y=160)
       e_senha.place(x=10,y=240)
       b_loguin.place(x=10)
       b_cadas.place(x=90)
       b_lista.place(x=180)


    def adicionar():
        adici_nome = e_nomecada.get()
        adicio_senha = senhacadas.get()
        adici_email = e_email.get()
        adici_loguin = e_usuario.get()
        #colocar um nome usuario

        if adici_nome == '' or adici_email == '' or adici_loguin == '' or adicio_senha == ' ':
            messagebox.showinfo("erro ao inserit",message="preencha todoas campos")

        else:
            banco.sql.execute('''
            insert into login(nome,email,login,senha) values(?,?,?,?)
            ''',(adici_nome,adici_email,adici_loguin,adicio_senha))
            #limpar campos
            e_nomecada.delete(0,END)
            e_email.delete(0,END)
            listabox.delete(0,END)
            senhacadas.delete(0,END)
            banco.con.commit()
            messagebox.showinfo(title="cadastro",message="cadastro realizado com sucesso")

    b_inser = Button(frame_dir,command=adicionar,text="Inserir",font=fonte)
    b_inser.place(x=10,y=340)

    b_voutar = Button(frame_dir,command=vouta, text="Voltar", font=fonte)
    b_voutar.place(x=90, y=340)

def verlista():
    listabox.delete(0,END)
    banco.sql.execute("SELECT  nome,email,login from login")
    usuario = banco.sql.fetchall()

    if usuario:
        for usua in usuario:
            nome,email,login = usua
            listabox.insert(END,f"Nome: {nome} | Email:{email}|Loguim{login}")
    else:
        listabox.insert(END,"Nenhum Usuario cadastrado!")




#logar no sistema
def autentica():
    veri_loguin = e_nome.get()
    veri_senha = e_senha.get()
    print(veri_loguin, veri_senha)
    banco.sql.execute("""
    SELECT * FROM login WHERE (login =? and senha =?)""",(veri_loguin,veri_senha))
    dados_banco = banco.sql.fetchone()
    try:
        if veri_loguin in dados_banco and veri_senha in dados_banco:
            messagebox.showinfo(title="login",message=f"seja bem vindo: {veri_loguin}")
            e_nome.delete(0,END)
            e_senha.delete(0,END)

    except:
        messagebox.showinfo(title="login",message=f"Usuario inexistente: {veri_loguin}")
        e_nome.delete(0, END)
        e_senha.delete(0, END)


#frame esquerdo
frame_esq = Frame(janela,width=270,height=400,bg=preto)
frame_esq.place(x=0,y=0)

#frame direito
frame_dir = Frame(janela,width=270,height=400,bg=cinza)
frame_dir.place(x=280,y=0)

#lista
listabox = Listbox(frame_dir,width=40,height=7,bg=branco)
listabox.place(x=5,y=6)


#imagem
logo = PhotoImage(file="cavale.png")
logol = Label(frame_esq,image=logo,bg=preto)
logol.place(x=0,y=0)

#loguin
nome = Label(frame_dir,text="Nome",font=fonte,bg=cinza,fg=branco)
nome.place(x=10,y=130)

e_nome = Entry(frame_dir,width=15,font=fonte)
e_nome.place(x=10,y=160)

senha = Label(frame_dir,text="Senha",font=fonte,bg=cinza,fg=branco)
senha.place(x=10,y=210)

e_senha = Entry(frame_dir,width=15,font=fonte)
e_senha.place(x=10,y=240)

b_loguin = Button(frame_dir,command=autentica,text="login",font=fonte)
b_loguin.place(x=10,y=290)

b_cadas = Button(frame_dir,command=cadastro,text="cadastro",font=fonte)
b_cadas.place(x=90,y=290)

b_lista = Button(frame_dir,command=verlista,text="lista",font=fonte)
b_lista.place(x=180,y=290)

janela.mainloop()