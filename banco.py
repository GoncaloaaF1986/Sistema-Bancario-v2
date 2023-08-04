from dataclasses import dataclass
from enum import Enum

class TipoMov(Enum):
    LEV = ("Levantamento","-")
    DEP = ("Deposito", "+")

@dataclass
class Movimetos:
    valor: float
    tipo: TipoMov

    def toString(self) -> str :
        return f"{self.tipo.value[0]}:{self.tipo.value[1]}{self.valor:.2f}"

class Conta:

    def __init__(self, id):
        self.id = id
        self.saldo = 0
        self.movimentos = []

    def levantar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.movimentos.append(Movimetos(valor, TipoMov.LEV))
            return valor
        else:
            return 0

    def depositar(self, valor):
        self.saldo += valor
        self.movimentos.append(Movimetos(valor, TipoMov.DEP))

    def getExtrato(self):

        extrato = f"Extrato conta {self.id}".center(30, "-")
        extrato += "\n"
        for i in self.movimentos:
            extrato += i.toString()
            extrato += "\n"
        extrato += f"saldo atual: {self.saldo:.2f}"
        extrato += "\n\n"
        extrato += "Fim de Extrato".center(30, "-")
        return extrato

    def __eq__(self, other):
        return self.id == other



class Banco:
    def __init__(self):
        self.contas = []

    def cirar_conta(self, id_conta):
        self.contas.append(Conta(id_conta))


    def movimentar_conta(self, conta_id:int, tipo_movimento:TipoMov, valor:float):
       try:
            conta_selec = self.contas.index(conta_id)

            conta_selec: Conta = self.contas[conta_selec]

            if tipo_movimento == TipoMov.LEV:
                conta_selec.levantar(valor)
                return valor
            else:
                conta_selec.depositar(valor)

            return True
       except:
           return False

    def get_estrato(self, id_conta) -> str:
        try:
            conta_selec = self.contas.index(id_conta)

            conta_selec: Conta = self.contas[conta_selec]

            return conta_selec.getExtrato()

        except:
            return "A Conta nao Existe"
