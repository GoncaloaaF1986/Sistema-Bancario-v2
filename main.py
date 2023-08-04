from banco import Banco, TipoMov, Conta

b = Banco()

b.cirar_conta(10)
b.cirar_conta(12)

b.movimentar_conta(10,TipoMov.DEP, 10)
b.movimentar_conta(12,TipoMov.DEP, 10)
b.movimentar_conta(10,TipoMov.DEP, 50)
b.movimentar_conta(10,TipoMov.LEV, 30)
b.movimentar_conta(10,TipoMov.DEP, 40)

print(b.get_estrato(10))
print(b.get_estrato(12))