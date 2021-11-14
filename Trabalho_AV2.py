import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import Tk, Label, StringVar, Entry, Scrollbar, Button, Toplevel, Frame, TOP, LEFT, RIGHT, X, W, Y, BOTTOM, SOLID, HORIZONTAL, VERTICAL, NO, Menu
import sqlite3

root = Tk()
root.title("SIA - ESTÁCIO")
width = 900
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)

root.config(bg='#4169E1')

nome = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
avds = StringVar()
email = StringVar()
endereco = StringVar()
campus = StringVar()
periodo = StringVar()
matricula = None
updateWindow = None
newWindow = None

def database():
    conn = sqlite3.connect("BancoPython\Trabalho_AV2\estacio.db")
    cursor = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS Aluno(
                        matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        av1 FLOAT,
                        av2 FLOAT,
                        av3 FLOAT,
                        avd FLOAT,
                        avds FLOAT,
                        email TEXT,
                        endereco TEXT,
                        campus TEXT,
                        periodo TEXT)'''
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'Aluno' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def submit_data():
    if nome.get() == "" or email.get() == "" or endereco.get() == "":
        msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("BancoPython\Trabalho_AV2\estacio.db")
        cursor = conn.cursor()
        query = '''INSERT INTO Aluno (nome, av1, av2, av3, avd, avds, email, endereco, campus, periodo)  
                        VALUES (?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(query, (str(nome.get()), str(av1.get()), str(av2.get()), str(av3.get()), 
            str(avd.get()), str(avds.get()), str(email.get()), str(endereco.get()), str(campus.get()),str(periodo.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'Aluno' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        email.set("")
        endereco.set("")
        campus.set("")
        periodo.set("")

def update_data():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("BancoPython\Trabalho_AV2\estacio.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE Aluno set nome = ?, av1 = ?,  av2 = ?,  av3 = ?,  avd = ?,  avds = ?, email = ?, endereco = ?, campus = ?, periodo = ? WHERE matricula = ?''',
                   (str(nome.get()), str(av1.get()), str(av2.get()), str(av3.get()), str(avd.get()), str(avds.get()), str(email.get()), str(endereco.get()), str(campus.get()),str(periodo.get()), int(matricula)))
    conn.commit()
    cursor.execute("SELECT * FROM 'Aluno' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    email.set("")
    endereco.set("")
    campus.set("")
    periodo.set("")
    updateWindow.destroy()

def on_select(event):
    global matricula, updateWindow
    select_item = tree.focus()
    conteudo = (tree.item(select_item))
    selected_item = conteudo['values']
    matricula = selected_item[0]
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    email.set("")
    endereco.set("")
    campus.set("")
    periodo.set("")
    nome.set(selected_item[1])
    av1.set(selected_item[2])
    av2.set(selected_item[3])
    av3.set(selected_item[4])
    avd.set(selected_item[5])
    avds.set(selected_item[6])
    email.set(selected_item[7])
    endereco.set(selected_item[8])
    campus.set(selected_item[9])
    periodo.set(selected_item[10])

    updateWindow = Toplevel()
    updateWindow.title("ATUALIZANDO ALUNO ")
    form_titulo = Frame(updateWindow)
    form_titulo.pack(side=TOP)
    form_aluno = Frame(updateWindow)
    form_aluno.pack(side=TOP, pady=10)
    width = 400
    height = 405
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    lbl_title = Label(form_titulo, text="Atualizando alunos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(form_aluno, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(form_aluno, text='AV1', font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(form_aluno, text='AV2', font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(form_aluno, text='AV3', font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(form_aluno, text='AVD', font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(form_aluno, text='AVDS', font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)
    lbl_email = Label(form_aluno, text='Email', font=('arial', 12))
    lbl_email.grid(row=6, sticky=W)
    lbl_endereco = Label(form_aluno, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=7, sticky=W)
    lbl_campus = Label(form_aluno, text='Campus', font=('arial', 12))
    lbl_campus.grid(row=8, sticky=W)
    lbl_periodo = Label(form_aluno, text='Período', font=('arial', 12))
    lbl_periodo.grid(row=9, sticky=W)

    nome_entry = Entry(form_aluno, textvariable=nome, font=('arial', 12))
    nome_entry.grid(row=0, column=1)
    av1_entry = Entry(form_aluno, textvariable=av1, font=('arial', 12))
    av1_entry.grid(row=1, column=1)
    av2_entry = Entry(form_aluno, textvariable=av2, font=('arial', 12))
    av2_entry.grid(row=2, column=1)
    av3_entry = Entry(form_aluno, textvariable=av3, font=('arial', 12))
    av3_entry.grid(row=3, column=1)
    avd_entry = Entry(form_aluno, textvariable=avd, font=('arial', 12))
    avd_entry.grid(row=4, column=1)
    avds_entry = Entry(form_aluno, textvariable=avds, font=('arial', 12))
    avds_entry.grid(row=5, column=1)
    email_entry = Entry(form_aluno, textvariable=email, font=('arial', 12))
    email_entry.grid(row=6, column=1)
    endereco_entry = Entry(form_aluno, textvariable=endereco, font=('arial', 12))
    endereco_entry.grid(row=7, column=1)
    campus_entry = Entry(form_aluno, textvariable=campus, font=('arial', 12))
    campus_entry.grid(row=8, column=1)
    periodo_entry = Entry(form_aluno, textvariable=periodo, font=('arial', 12))
    periodo_entry.grid(row=9, column=1)

    bttn_updatecom = Button(form_aluno, text="Atualizar",
                            width=50, command=update_data)
    bttn_updatecom.grid(row=10, columnspan=2, pady=10)

def delete_data():
    if not tree.selection():
        msb.showwarning('', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion(
            '', 'Tem certeza que deseja deletar o aluno?')
        if resultado == 'yes':
            select_item = tree.focus()
            conteudo = (tree.item(select_item))
            selected_item = conteudo['values']
            tree.delete(select_item)
            conn = sqlite3.connect("BancoPython\Trabalho_AV2\estacio.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'Aluno' WHERE matricula = %d" %
                           selected_item[0])
            conn.commit()
            cursor.close()
            conn.close()

def insert_data():
    global newWindow
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    email.set("")
    endereco.set("")
    campus.set("")
    periodo.set("")

    newWindow = Toplevel()
    newWindow.title("CADASTRO DE ALUNO")
    form_titulo = Frame(newWindow)
    form_titulo.pack(side=TOP)
    form_aluno = Frame(newWindow)
    form_aluno.pack(side=TOP, pady=10)
    width = 400
    height = 405
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    lbl_title = Label(form_titulo, text="Inserindo alunos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    
    lbl_nome = Label(form_aluno, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(form_aluno, text='AV1', font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(form_aluno, text='AV2', font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(form_aluno, text='AV3', font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(form_aluno, text='AVD', font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(form_aluno, text='AVDS', font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)
    lbl_email = Label(form_aluno, text='Email', font=('arial', 12))
    lbl_email.grid(row=6, sticky=W)
    lbl_endereco = Label(form_aluno, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=7, sticky=W)
    lbl_campus = Label(form_aluno, text='Campus', font=('arial', 12))
    lbl_campus.grid(row=8, sticky=W)
    lbl_periodo = Label(form_aluno, text='Período', font=('arial', 12))
    lbl_periodo.grid(row=9, sticky=W)

    nome_entry = Entry(form_aluno, textvariable=nome, font=('arial', 12))
    nome_entry.grid(row=0, column=1)
    av1_entry = Entry(form_aluno, textvariable=av1, font=('arial', 12))
    av1_entry.grid(row=1, column=1)
    av2_entry = Entry(form_aluno, textvariable=av2, font=('arial', 12))
    av2_entry.grid(row=2, column=1)
    av3_entry = Entry(form_aluno, textvariable=av3, font=('arial', 12))
    av3_entry.grid(row=3, column=1)
    avd_entry = Entry(form_aluno, textvariable=avd, font=('arial', 12))
    avd_entry.grid(row=4, column=1)
    avds_entry = Entry(form_aluno, textvariable=avds, font=('arial', 12))
    avds_entry.grid(row=5, column=1)
    email_entry = Entry(form_aluno, textvariable=email, font=('arial', 12))
    email_entry.grid(row=6, column=1)
    endereco_entry = Entry(form_aluno, textvariable=endereco, font=('arial', 12))
    endereco_entry.grid(row=7, column=1)
    campus_entry = Entry(form_aluno, textvariable=campus, font=('arial', 12))
    campus_entry.grid(row=8, column=1)
    periodo_entry = Entry(form_aluno, textvariable=periodo, font=('arial', 12))
    periodo_entry.grid(row=9, column=1)

    bttn_submitcom = Button(form_aluno, text="Cadastrar",
                            width=50, command=submit_data)
    bttn_submitcom.grid(row=10, columnspan=2, pady=10)


top = Frame(root, width=700, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg='#4169E1')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="#4169E1")
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

lbl_title = Label(top, text="SISTEMA DE GERENCIAMENTO DE ALUNOS", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para alterar clique duas vezes no aluno desejado.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)


bttn_add = Button(midleft, text="Inserir", bg="#3CB371", command=insert_data)
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar",
                     bg="#B22222", command=delete_data)
bttn_delete.pack(side=RIGHT)

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("Matrícula", "Nome", "AV1", "AV2", "AV3", "AVD", "AVDS", "E-mail", "Endereço", "Campus", "Período"),
                    height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("Matrícula", text="Matrícula", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.heading("E-mail", text="E-mail", anchor=W)
tree.heading("Endereço", text="Endereço", anchor=W)
tree.heading("Campus", text="Campus", anchor=W)
tree.heading("Período", text="Período", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=60)
tree.column('#2', stretch=NO, minwidth=0, width=50)
tree.column('#3', stretch=NO, minwidth=0, width=40)
tree.column('#4', stretch=NO, minwidth=0, width=40)
tree.column('#5', stretch=NO, minwidth=0, width=40)
tree.column('#6', stretch=NO, minwidth=0, width=40)
tree.column('#7', stretch=NO, minwidth=0, width=40)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=85)
tree.column('#11', stretch=NO, minwidth=0, width=70)
tree.pack()
tree.bind('<Double-Button-1>', on_select)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Criar novo", command=insert_data)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.destroy)


if __name__ == '__main__':
    database()
    root.mainloop()