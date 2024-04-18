import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import time

class Cliente:
    def __init__(self, endereco):
	def adicionar_conta(self, conta):


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco, senha):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Endereço: {self.endereco}"

class Conta:
    def __init__(self, numero, cliente):
	def adicionar_transacao(self, transacao):
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

	def registrar(self, conta):
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Validações básicas
def nome_valido(nome):
    return nome.isalpha() and len(nome) >= 3

def senha_valida(senha):
    return len(senha) >= 6 and senha.isdigit()

def is_valid_cpf(cpf):
    # Remove any non-digit characters
    cpf = ''.join(filter(str.isdigit, cpf))

    # Check if it has exactly 11 digits and if they are all numbers
    return len(cpf) == 11 and cpf.isdigit()

def data_nascimento_valida(data_nascimento):
    try:
        # Attempt to parse the input date in the specified format
        datetime.strptime(data_nascimento, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
	def recuperar_conta_cliente(cliente):


def depositar(clientes):
    while True:
        cpf = input("Informe o CPF (somente números): ")
        if is_valid_cpf(cpf):
            print("CPF válido:", cpf)
            break
        else:
            print("CPF inválido. Certifique-se de inserir apenas 11 dígitos numéricos.")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
	def depositar(clientes):


def sacar(clientes):
    while True:
        cpf = input("Informe o CPF (somente números): ")
        if is_valid_cpf(cpf):
            print("CPF válido:", cpf)
            break
        else:
            print("CPF inválido. Certifique-se de inserir apenas 11 dígitos numéricos.")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
	def sacar(clientes):


def exibir_extrato(clientes):
    while True:
        cpf = input("Informe o CPF (somente números): ")
        if is_valid_cpf(cpf):
            print("CPF válido:", cpf)
            break
        else:
            print("CPF inválido. Certifique-se de inserir apenas 11 dígitos numéricos.")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
	def exibir_extrato(clientes):


def criar_cliente(clientes):
    while True:
        while True:
            cpf = input("Informe o CPF (somente números): ")
            if is_valid_cpf(cpf):
                print("CPF válido:", cpf)
                break
            else:
                print("CPF inválido. Certifique-se de inserir apenas 11 dígitos numéricos.")

        cliente = filtrar_cliente(cpf, clientes)

        if cliente:
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return

        while True:
            nome = input("Informe o nome completo (mínimo de 3 letras): ")
            if nome_valido(nome):
                print("Nome válido:", nome)
                break
            else:
                print("Nome inválido. Certifique-se de inserir apenas letras e ter no mínimo 3 caracteres.")

        while True:
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            if data_nascimento_valida(data_nascimento):
                print("Data de nascimento válida:", data_nascimento)
                break
            else:
                print("Data de nascimento inválida. Certifique-se de inserir no formato dd-mm-aaaa.")

        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        while True:
            senha = input("Informe sua Senha(minimo de 6 digitos, apenas números): ")
            if senha_valida(senha):
                nao_mostrar = "*" * len(senha)
                print("Senha valida:", nao_mostrar)
                break
            else:
                print("Senha inválida. Minimo de 6 dígitos numéricos.")

        # Display the client's information for confirmation
        print("\n=== Informações do Cliente ===")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Data de Nascimento: {data_nascimento}")
        print(f"Endereço: {endereco}")

        confirmation = input("As informações inseridas estão corretas? (S/N) ").strip().lower()
        if confirmation == "s":
            cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, senha=senha)
            clientes.append(cliente)
            print("\n=== Cliente criado com sucesso! ===")
            break
        elif confirmation == "n":
            print("Por favor, reinsira as informações do cliente.")
        else:
            print("Resposta inválida. Responda 'S' para confirmar ou 'N' para reentrar as informações.")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF (somente números): ")
    if is_valid_cpf(cpf):
        print("CPF válido:", cpf)
    else:
        print("CPF inválido. Certifique-se de inserir apenas 11 dígitos numéricos.")
        return
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
	def criar_conta(numero_conta, clientes, contas):
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print(conta)

    print("\n=== Conta criada com sucesso! ===")

	def listar_contas(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def sign():
    sign = """\n
    ============= SIGN PAGE =============
    \t[i] Sign In
    \t[c] Sign Up
    \t[q] Sair
    => """
    return input(sign)

def authenticate(clientes):
    attempt_count = 0
    while True:
        value = sign()
        if value == "i":
            password_attempt = input("Digite sua senha: ")
            if any(cliente.senha == password_attempt for cliente in clientes):
                return password_attempt
            else:
                attempt_count += 1
                if attempt_count >= 5:
                    exit()
                elif attempt_count >= 3:
                    print("Senha incorreta. Você excedeu o limite de tentativas. Tente novamente em 30 minutos.")
                    time.sleep(5)  # Sleep for 30 minutes (1800 seconds)
                else:
                    print("Senha incorreta. Tente novamente.")
        elif value == "c":
            criar_cliente(clientes)
            password_attempt = input("Digite sua senha: ")
            if any(cliente.senha == password_attempt for cliente in clientes):
                return password_attempt
            else:
                print("Senha incorreta. Tente novamente.")
        elif value == "q":
            exit()
        else:
            print("Opção inválida. Por favor, selecione 'i' para SignIn ou 'c' para SignUp.")

def main():
    clientes = []
    authenticated = False
    while not authenticated:
        password_attempt = authenticate(clientes)
        if any(cliente.senha == password_attempt for cliente in clientes):
            authenticated = True
        else:
            print("Senha incorreta. Tente novamente.")

    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()
