from modules.Cliente import *

cliente = Cliente('Mauro', 25, 'Maipu 1452', 45948545)

print(cliente)

cliente.addProductToCart('Monitor', 2)
cliente.addProductToCart('Mouse', 15)
cliente.addProductToCart('Teclado', 15)
cliente.addProductToCart('Otro', 15)
cliente.removeProductFromCart('Otro')

cliente.showCart()
print("")
cliente.buy()
print("")
cliente.showCart()