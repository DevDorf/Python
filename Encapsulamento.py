class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0 # atributo privado

    @property # Propriedade funciona como Método acessor
    def saldo(self):
        return self.__saldo


    def depositar(self, valor):
        if valor < 0:
            return 'O valor deve ser positivo'
        self.__saldo += valor
        return 'Deposito Reaizado com Sucesso'


    def sacar(self, valor):
        if valor < 0:
            return ('Valor deve ser psitivo')
        if valor > self.__saldo:
            return 'Saldo Insuficiente'
        self.__saldo -= valor
        return 'Saque Realizado com Sucesso'


if __name__ == '__main__':
    conta1 = Conta(1, 'Caio')

