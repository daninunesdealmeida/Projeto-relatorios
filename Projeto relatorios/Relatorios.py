import psycopg2
import csv

connection = psycopg2.connect(user="postgres",
                              password="3258",
                              host="localhost",
                              port="5432",
                              database="projeto")
cursor = connection.cursor()


def relatorio01():
    # ************ Conexão e Query ************
    cursor = connection.cursor()
    cursor.execute("""select livro.titulo, autor.nome, editora.nome, endereco.pais, endereco.estado, livro.publicacao, livro.valor
    from livro, editora, endereco, autor
    where endereco.codendereco = editora.codeditora and 
    autor.codautor = livro.autor and
    editora.codeditora = livro.editora and
    publicacao > '31-12-2013'""")

    # ************ busca itens ************
    con = cursor.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio01.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Título do Livro', 'Nome do Autor', 'Nome da Editora', 'Pais da Editora', 'Estado da Editora',
           'Data Publicação', 'Valor']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor.close()


def relatorio02A():
    # *********** Conexão e Query *************
    cursor = connection.cursor()
    cursor.execute("""select livro.titulo, autor.nome, editora.nome, livro.publicacao, 
    livro.valor, livro.edicao, livro.idioma
    from livro, autor, editora
    where editora.codeditora = livro.editora and
    autor.codautor = livro.autor 
    order by valor desc limit 3; """)

    # ************ busca itens ************
    con = cursor.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio02A.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Nome do Livro', 'Nome do Autor', 'Nome da Editora', 'Data Publicação', 'Valor', 'Edição', 'Idioma']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor.close()


def relatorio02B():
    # ************ Conexão e Query ************
    cursor2 = connection.cursor()
    cursor2.execute("""select livro.titulo, autor.nome, editora.nome, livro.publicacao, 
    livro.valor, livro.edicao, livro.idioma
    from livro, autor, editora
    where editora.codeditora = livro.editora and
    autor.codautor = livro.autor 
    order by livro.publicacao asc limit 3; """)

    # ************ busca itens ************
    con = cursor2.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio02B.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Nome do Livro', 'Nome do Autor', 'Nome da Editora', 'Data Publicação', 'Valor', 'Edição', 'Idioma']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor2.close()


def relatorio02C():
    # ************ Conexão e Query ************
    cursor3 = connection.cursor()
    cursor3.execute("""select livro.titulo, autor.nome, editora.nome, livro.publicacao, 
    livro.valor, livro.edicao, livro.idioma
    from livro, autor, editora
    where editora.codeditora = livro.editora and
    autor.codautor = livro.autor 
    order by livro.publicacao desc limit 3; """)

    # ************ busca itens ************
    con = cursor3.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio02C.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Nome do Livro', 'Nome do Autor', 'Nome da Editora', 'Data Publicação', 'Valor', 'Edição', 'Idioma']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor3.close()


def relatorio02D():
    # ************ Conexão e Query ************
    cursor4 = connection.cursor()
    cursor4.execute("""(select livro.titulo, autor.nome, editora.nome, livro.publicacao, 
                            livro.valor, livro.edicao, livro.idioma
                            from livro, autor, editora
 							where editora.codeditora = livro.editora and
							autor.codautor = livro.autor and
                            trim(idioma) like 'portugues%'
                            order by livro.valor desc limit 3)
                            union all
                            (select livro.titulo, autor.nome, editora.nome, livro.publicacao, 
                            livro.valor, livro.edicao, livro.idioma
                            from livro, autor, editora
							where editora.codeditora = livro.editora and
							autor.codautor = livro.autor and
                            trim(idioma) like 'ingl%'
                            order by livro.valor desc limit 3)""")

    # ************ busca itens ************
    con = cursor4.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio02D.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Nome do Livro', 'Nome do Autor', 'Nome da Editora', 'Data Publicação', 'Valor', 'Edição', 'Idioma']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor4.close()


def relatorio03():
    # ************ Conexão e Query ************
    cursor = connection.cursor()
    cursor.execute("""select a.nome, count(l.publicacao), sum(l.valor) 
    from livro l inner join autor a on l.autor=a.codautor
    group by a.nome""")

    # ************ busca itens ************
    con = cursor.fetchall()

    # ************ gera o csv ************
    gerador = csv.writer(open('relatorio03.csv', 'w', newline='', encoding="utf-8"))

    # ************ cabecalho ************
    cab = ['Nome do Autor', 'Quantidade de Publicações', 'Valor Total das Publicações do Autor']
    gerador.writerow(cab)

    # ************ loop de dados ************
    for con in con:
        gerador.writerow(con)

    cursor.close()


# ************ INTERFACE ***************
from tkinter import *

# ********** Cria a janela ***********
window = Tk()

window.title("Compasso Reports")
window.configure(background="Gray89")
window.geometry('500x650')
window.iconbitmap(r'compasso.ico')

# ******** Apresenta imagem na tela **********
photo = PhotoImage(file="logo.png")
label = Label(window, image=photo)
label.config(image=photo, width="100", height="100")
label.pack()

# ************* Espaço **************
label1 = Label(window, text="")
label1.pack()

# ************** Botão 1 *************
label2 = Label(window, text="Livros após 2014")
label2.pack()

btn = Button(window, text="Gerar Relatório", bg="grey", fg="white")
btn.config(width=27, height=3)
btn.pack()
btn.config(command=relatorio01)

# ************ Botão 2A ************
label3 = Label(window, text="Top 3 livros mais caros")
label3.pack()

btn2 = Button(window, text="Gerar Relatório", bg="black", fg="white")
btn2.config(width=27, height=3)
btn2.pack()
btn2.config(command=relatorio02A)

# ************ Botão 2B ************
label3 = Label(window, text="Top 3 livros mais antigos")
label3.pack()

btn3 = Button(window, text="Gerar Relatório", bg="grey", fg="white")
btn3.config(width=27, height=3)
btn3.pack()
btn3.config(command=relatorio02B)

# ************ Botão 2C ************
label4 = Label(window, text="Top 3 livros mais novos")
label4.pack()

btn4 = Button(window, text="Gerar Relatório", bg="black", fg="white")
btn4.config(width=27, height=3)
btn4.pack()
btn4.config(command=relatorio02C)

# ************ Botão 2D ************
label5 = Label(window, text="Top 3 livros mais caros por idioma")
label5.pack()

btn5 = Button(window, text="Gerar Relatório", bg="grey", fg="white")
btn5.config(width=27, height=3)
btn5.pack()
btn5.config(command=relatorio02D)

# ********** Botão 3 ***********
label6 = Label(window, text="Nº de publicações por autor")
label6.pack()

bt = Button(window, text="Gerar Relatório", bg="black", fg="white")
bt.config(width=27, height=3)
bt.pack()
bt.config(command=relatorio03)

# ********** Fecha janela ***********
window.mainloop()
