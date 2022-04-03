class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite


    def retirar(self, saque):
        if self.saldo - saque < self.limite:
            print('saldo insuficiente')
        else:
            self.saldo -= saque

    def guardar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
        else:
            print('deposito tem que ser maior que zero')

    def consulta_saldo(self):
        return self.saldo







