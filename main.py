import sqlite3
from tkinter import messagebox

class sistema_de_registro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS estudantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                tel TEXT NOT NULL,
                sexo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                endereco TEXT NOT NULL,
                curso TEXT NOT NULL,
                picture TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def cadastrar_estudante(self, estudantes):
        self.cursor.execute('''
            INSERT INTO estudantes (nome, email, tel, sexo, data_nascimento, endereco, curso, picture)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (estudantes))
        self.conn.commit()
        messagebox.showinfo("Sucesso", "Estudante cadastrado com sucesso!")

    def buscar_estudante(self, id):
        self.cursor.execute('SELECT * FROM estudantes WHERE id=?', (id,))
        estudante = self.cursor.fetchone()

        if estudante:
            print(f"""
                ID: {estudante[0]}, 
                Nome: {estudante[1]}, 
                Email: {estudante[2]}, 
                Telefone: {estudante[3]}, 
                Sexo: {estudante[4]}, 
                Data de Nascimento: {estudante[5]}, 
                Endereço: {estudante[6]}, 
                Curso: {estudante[7]}, 
                Picture: {estudante[8]}""")
            return estudante
        else:
            print("Estudante não encontrado.")
            return None
        
    
    def buscar_todos_estudantes(self):
        self.cursor.execute('SELECT * FROM estudantes')
        estudantes = self.cursor.fetchall()

        for estudante in estudantes:
            print(f"ID: {estudante[0]}, Nome: {estudante[1]}, Email: {estudante[2]}, Telefone: {estudante[3]}, Sexo: {estudante[4]}, Data de Nascimento: {estudante[5]}, Endereço: {estudante[6]}, Curso: {estudante[7]}, Picture: {estudante[8]}")

        return estudantes
    
    def deletar_estudante(self, id):
        self.cursor.execute('DELETE FROM estudantes WHERE id=?', (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Estudante com ID: {id} foi deletado com sucesso!")

    def atualizar_estudante(self, estudante):
        self.cursor.execute('''
            UPDATE estudantes
            SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=?
            WHERE id=?
        ''', (estudante))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Estudante com ID: {estudante[8]} foi atualizado com sucesso!")

# Criando uma instância da classe sistema_de_registro
sistema = sistema_de_registro()

# informações do estudante
# estudante = ("João", "joao@example.com", "123456789", "M", "01/01/2000", "Rua A, 123", "Engenharia", "picture.jpg")
# estudante2 = ("Maria Joana", "maria@example.com", "987654321", "F", "02/02/2001", "Rua B, 456", "Medicina", "picture2.jpg")
estudante_edit = ("Maria Joana", "maria@example.com", "987654321", "F", "02/02/2001", "Rua B, 456", "Medicina", "picture2.jpg", 2)

# sistema.cadastrar_estudante(estudante)
# sistema.cadastrar_estudante(estudante2)

# sistema.buscar_estudante(1)
sistema.buscar_todos_estudantes()

# sistema.atualizar_estudante(estudante_edit)
sistema.deletar_estudante(1)
sistema.buscar_todos_estudantes()
