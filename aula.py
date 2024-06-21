from abc import ABC,abstractclassmethod,abstractproperty
import datetime


class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []

    def realizar_transaçao(self, conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class pessoa_fisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = extrato()
        self.agencia = "1234"

    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def extrato(self):
        return self._extrato
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def agencia(self):
        return self._agencia
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado")
            return True
        else:
            print("Valor inválido!")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado")
        else:
            print("Valor inválido!")
            return False
        
        return True    

class Conta_Corrente(conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.extrato.transacoes if transacao["tipo"] == "Saques"]
        )
         
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numeros_de_saques >= self.limite_saque

        if excedeu_limite:
            print("Valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Número máximo de saques.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t {self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class extrato:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "hora": datetime.datetime.now().strftime("%H:%M:%S"),
                "dia": datetime.datetime.now().strftime("%d/%m/%Y"),
                "mes": datetime.datetime.now().strftime("%m/%Y"),
            }
        )

class transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class saque(transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.extrato.adicionar_transacao(self)

class deposito(transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.extrato.adicionar_transacao(self)