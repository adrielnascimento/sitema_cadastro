import sqlite3
banco = sqlite3.connect("Sistema Cadastral")
cursor = banco.cursor()
#codigo da criação da tabela 
#cursor.execute("CREATE TABLE cadastro (cpf char (11), nome varchar (20), email varchar (30), senha (varchar 10)")
class Cadastro:
    # veroficar se essa pessoa existe no banco
    def verificar_cadastro(self, cpf):
        try:  
            cursor.execute("SELECT nome from cadastro where cpf = ?", (cpf,))
            resultado = cursor.fetchall()
            if resultado:
                nome = resultado[0][0]
                print(f"CPF encontrado com o nome  de {nome}")
                print("seja bem vindo!")
                return True
            else: 
                print(f"NENHUM NOME ENCONTRADO COM O CPF: {cpf}")              
                print("PRIMEIRO REALIZE O SEU CADASTRO")
                resp = input('Deseja realizar seu cadastro? [sim/ não]')
                if resp.lower() in ['sim', 's']: 
                    nome = input('nome: ')
                    email = input('email: ')
                    senha = input('senha: ')
                    self.cadastrar(nome, email, cpf, senha)
                return False
        except sqlite3.Error as erro: 
            print(f"ERRO {erro} ao realizar a consulta")
        return False
    
    # cadastrar
    def cadastrar(self, nome, email, cpf, senha):
        try:
            if not self.verificar_cadastro(cpf): 
                cursor.execute("INSERT INTO cadastro VALUES (?, ?, ?, ?)", (cpf, nome, email, senha))
                print(f"Usuario {nome} cadastrado com sucesso.")
                banco.commit()
            else: 
                print('USUARIO JA EXISTENTE!')

        except sqlite3.Error as erro:
            print(f'ERRO {erro} ao inserir os dados')

    def delet_user(self, cpf):
        cursor.execute("DELETE FROM cadastro WHERE cpf = (?)", (cpf))
        print('usuario deletado com sucesso!')

    # desconectar do banco
    def desc_banco(self):
        banco.close()





