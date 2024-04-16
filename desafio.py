import textwrap

def menu() = 
    """\n
    =======================MENU===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
    
def depositar(saldo,valor,extrato,/):
    
def sacar(*,saldo,valor,extrato,limite,n_saques,l_saques):
def exibir_extrato(saldo,/*,extrato):
def criar_usuarios(usuarios):
def filtrar_usuario(cpf,usuarios):
def criar_conta(agencia,n_conta,usuarios):
def listar_contas(contas):
def main():
    LIMITE_SAQUES=3
    AGENCIA="001"
    
    saldo=0
    limite=500
    extrato=""
    n_saques=0
    usuarios=""
    contas=""
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo,extrato= depositar(saldo,valor,extrato)
                
    
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
    
            saldo,extrato=sacar(
                 saldo=saldo,
                 valor=valor,
                 extrato=extrato,
                 limite=limite,
                 n_saques=n_saques,
                 limite_saques=LIMITE_SAQUES)
            
                 
    
        elif opcao == "e":
             exibir_extrato(saldo,extrato=extrato)
            
        elif opcao == "nu":
             criar_usuario(usuarios) 
            
        elif opcao == "nc":
             n_conta=len(contas)
         elif opcao == "lc":
             listar_contas(contas)
    
        elif opcao == "q":
            break
    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()


