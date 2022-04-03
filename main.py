from clientes import Clientes
from conta import Conta

cliente1 = Clientes('jessica', '06237365940', 30)

conta_da_jessica = Conta(cliente1, 50.75, 1000)

print(conta_da_jessica.consulta_saldo())

conta_da_jessica.guardar(20)

print(conta_da_jessica.consulta_saldo())

conta_da_jessica.retirar(55.57)

print(conta_da_jessica.consulta_saldo())

conta_da_jessica.retirar(10)

print(conta_da_jessica.consulta_saldo())

conta_da_jessica.guardar(-454)

print(conta_da_jessica.consulta_saldo())

conta_da_jessica.guardar(50)

print(conta_da_jessica.consulta_saldo())





