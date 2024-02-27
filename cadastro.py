from classe_cadastro import Cadastro
import re


# validador de email
def validar_email(email):
    email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_padrao, email):
        return True
    else:
        return False
    
def main(): 
    print("SISTEMA DE CADASTRO")
    op = input('Você já está cadastrado no nosso sistema? [sim/ não]')
    if op.lower() in ['sim', 's']: 
        validador = False
        while not validador:
            cpf = input("Informe seu cpf: ")
            if len(cpf) == 11 and cpf.isdigit():
                u1 = Cadastro()
                u1.verificar_cadastro(cpf)
                validador = True
            else:
                print("ERRO! digite seu cpf corretamente (11 dígitos numericos)")
    if op.lower() in ['não', 'n']: 
        resp = input('Deseja realizar seu cadastro? [sim/ não]')
        if resp.lower() in ['sim', 's']:
            print("Digite seu...") 
            nome = input('nome: ')
            while True:
                cpf = input('cpf: ')
                if len(cpf) == 11 and cpf.isdigit(): 
                    break
                else: 
                    print("ERRO! digite seu cpf corretamente (11 dígitos numericos)")
            while True: 
                email = input('email: ')
                if validar_email(email):
                    break
                else:
                    print('email inválido')
            print("Digite sua senha lembre-se sua senha poderá ter apenas 10 dígitos")
            while True: 
                senha = input('senha: ')
                if len(senha) >= 11: 
                    print('Por favor, digite uma senha válida.')
                else: 
                    break
            u1 = Cadastro()
            u1.cadastrar(nome, email, cpf, senha) 
            u1.desc_banco()
        else: 
            print("Encerramento do programa de cadastro")
            
if __name__ == "__main__":
    main()
    