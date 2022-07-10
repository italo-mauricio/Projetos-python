
import os
import validacoes
from time import sleep




#DICIONÁRIO USADO PARA FACILITAR OS TESTES
#IREMOS SALVAR EM ARQUIVO FUTURAMENTE
dicionario = {
               
            '161.797.240-16': ['Erick Bezerra Ribeiro Trindade', '04/06/2003', 'erickbrtrindade@gmail.com', 'Rua Olegário Vale 1290 Centro', ''],
            '376.431.910-00': ['Manuelly Rodrigues Victor', '24/06/2000', 'manuellyrodrigues@gmail.com', 'Rua Capitão antonio Martins 88', 'apartamento'],
            '059.509.594-18': ['Italo Mauricio ', '30/30/1998', 'italomauricio@gmail.com', 'Rua dos Potros 1340', 'casa']

            }

#função de cadastro do cliente.
def cadastrocliente():
    os.system('cls')
    
    print('''Bem vindo ao nosso Sistema Integrado!
        Aqui você será muito bem atendido
        Vamos cadastrar você em instantes!
        Carregando...
    ''')
    sleep(1)
    nome = input("Por favor, digite o nome do cliente: ") #aqui o cliente digita o seu nome
    nascimento = input("Digite a data de nascimmento do cliente: ") #aqui o cliente digita a sua data de nascimento
    email = input("Digite o email do cliente: ") #aqui o cliente digita o seu email
    endereco = input("Digite o endereço do cliente: ") #aqui o cliente irá digitar o seu endereço
    complemento = input("Digite o complemento(Opcional): ") #aqui caso o cliente queira digitar um complemento


#recebe o CPF e valida, se for validado é adicionado como chave no dicionário para acesso as informações do cliente como: nome, nascimento, email, endereço e complemento.
    cpf = input("Por favor, digite um CPF válido: ") #aqui o cliente vai digitar o seu cpf
    while cpf != validacoes: #condicional de verificação de validade
        
        if cpf not in dicionario: #caso ele não esteja no dicionário, ele irá colocar
            dicionario[cpf] = [nome,nascimento,email,endereco,complemento] #dicionário recebe as informações
            print(dicionario[cpf]) #irá mostrar o dicionário
            print('Parabéns, você foi cadastrado com sucesso!')
            break
        else:
            cpf == dicionario #caso o cpf digitado for igual a algum já cadastrado, retorna o erro.
            print('CPF Já registrado, tente novamente!')
            return False
    
    telaprincipalcliente()




#Essa função é responsável por atualizar os dados do cliente a partir da chave
def atualizarcliente():
    os.system('cls')
#optamos por alterar cada item de forma separada a partir de uma posição no dicionário pré determinada no cadastro 
    print('''Olá, você está na sessão de atualização de cadastro.
             Vamos atualizar seu cadastro em instantes!
             Carregando...   
          ''')
    sleep(1)
    cpf = input("Por favor, insira um CPF já cadastrado: ")#cliente vai digitar qual cpf ele cadastrou
    if cpf in dicionario.keys(): #se ele estiver no dicionário ele entra
        print(dicionario[cpf][0]) #exibe o dicionário
        if cpf in dicionario.keys(): #se o cpf estiver no dicionário ele entra
            print('Perfeito, localizamos o cliente no nosso sistema!')
            sleep(1)
            cadastro_novo = ' '
            cadastro_novo = input('Digite qual informação você deseja atualizar: ').upper() #cliente digita qual informação ele quer alterar
            if cadastro_novo == 'nome'.upper(): #caso ele queira o nome, irá entrar na parte de alteração do nome
                nome_novo = input('Digite um novo nome: ') #ele insere o novo nome
                dicionario[cpf][0] = nome_novo # o novo nome vai ser inserido no dicionário
                print('Nome atualizado com sucesso!')
                print(f'O novo nome cadastrado é {nome_novo}') #exibe o novo nome cadastrado
                return True   
            if cadastro_novo == 'data de nascimento'.upper(): #caso ele queira a data de nascimento, ele entra na parte de alteração da data de nascimento.
                data_novo = input('Digite uma nova data de nascimento: ') # digita a nova data de nascimento
                dicionario[cpf][1] = data_novo # armazena no dicionário posição data a nova data
                print('Sua data de nascimento foi atualizada!')
                print(f'Sua nova data de nascimento é {data_novo}')# exibe a nova data de nascimento
                return True
            if cadastro_novo == 'email'.upper(): #caso ele queira mudar o email, ele entra na parte de alteração de email
                email_novo = input('Digite um novo email: ') # digita o novo email
                dicionario[cpf][2] = email_novo # novo email é adicionado na posição email
                print('Seu email foi atualizado com sucesso!')
                print(f'Seu novo email é {email_novo}') # exibe o email novo
                return True
            if cadastro_novo == 'endereço'.upper(): # caso ele queira alterar o seu endereço, entra na parte de alteração de endereço
                endereco_novo = input('Digite seu novo endereço: ') # digita o endereço novo
                dicionario[cpf][3] = endereco_novo # adiciona a lista o novo endereço digitado
                print("Seu endereço foi atualizado!")
                print(f'Seu novo endereço é {endereco_novo}') # exibe o novo endereço de email
                return True
            if cadastro_novo == 'opcional endereço'.upper(): # caso ele queria adicionar algum endereço opcional
                opendereco_novo = input('Digite seu endereço opcional novo: ') # digita o novo endereço opcional
                dicionario[cpf][4] = opendereco_novo # adiciona o endereço opcional ao dicionário
                print("Seu endereço opcional foi atualizado com sucesso!")
                print(f'Seu novo endereço opcional é {opendereco_novo}') # exibe o novo endereço opcional
                return True
            else:
                print('Opção inválida, por favor tente novamente!') # caso digite uma opção não condizente com os ifs
                return False
        print('Obrigado pela preferência de sempre!')
            
            
    else:
        print('Usuário não cadastrado, tente novamente!') # caso o cpf não esteja cadastrado no sistema
        return False

        
        


#Essa função é responsável por visualizar os dados do Cliente.   
def visualizarcliente():
    os.system('cls')
    print('''Olá, você escolheu a opção de visualizar um usuário já cadastrado!
            Para isso precisamos de um CPF cálido de usuário!
            Carregando..
        ''')
    sleep(1)
    cpf = input('Digite o CPF que foi cadastrado por gentileza!: ') # cliente digita qual cliente quer visualizar a partir de seu cpf
    while cpf != dicionario: #enquanto o cpf for diferente de dicionário, ele entra
        if cpf in dicionario: # se o cpf estiver no dicionário ele encontra o cliente
            print("Cliente encontrado!")
            print(dicionario[cpf])
            print(f'Cliente encontrado foi {cpf}')
            break 
        else:
            cpf not in dicionario # se ele não estiver no dicionário, ele retorna a mensagem
            print('Cliente não cadastrado!')
            return True
    telaprincipalcliente()   
       

    




#Essa função deleta qualquer cliente do banco de dados, a partir da chave do CPF
def deletarcliente():
    os.system('cls')
    print(''' Olá, você deseja apagar um banco de dados!
              Em instantes vamos realizar esta operação!
              Carregando
        ''')
    sleep(1)
    cliente = input('Por favor, digite o CPF do cliente que você deseja apagar: ') # cliente vai digitar o cpf que ele quer tirar do sistema
    if cliente in dicionario: # se ele estiver no dicionário (sistema)
        del dicionario[cliente] # deleta o cliente
        print('Perfeito, usuário encontrado e excluído com sucesso!')
        print(f'cliente deletado foi {dicionario[cliente]}') # exibe qual cliente foi deletado
        return True
    else:
        print("Infelizmente não encontramos este usuário em nosso sistema!") # caso não exista o usuário no sistema
        return False    





#Função de chamada da tela principal de menu clientes
def telaprincipalcliente(): # Aréa do cliente
    os.system('cls')
    
    print('=='*28)
    print('''
        = SISTEMA DE GERENCIAMENTO DE CLIENTES =
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ===== Cadastrar Cliente [1] ============ 
        ===== Atualizar Dados   [2] ============
        ===== Visualizar Dados  [3] ============
        ===== Remover Dados     [4] ============
        ===== Sair do Sistema   [5] ============
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ========================================
    ''')
    print('=='*28)

    usuário = input('Por favor, escolha uma das 5 opções: ')
    while usuário != "5":

        if usuário == '1': # se ele quiser se cadastrar no sistema digita 1
            cadastrocliente()
        elif usuário == '2': # se ele quiser atualizar alguma informação no sistema digita 2
            atualizarcliente()
        elif usuário == '3': # se ele quiser visualizar alguma informação no sistema digita 3
            visualizarcliente()
        elif usuário == '4': # se ele quiser deletar o seu perfil no sistema digita 4
            deletarcliente()
        elif usuário == '5':
            print('Obrigado, volte sempre!') # caso queira sair, digita 5
            break
        else:
            print('Opção inválida!') # caso digite qualquer outra opção, retorna inválida
            return False 

        










    