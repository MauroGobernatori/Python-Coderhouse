class Cliente:
    def __init__(self, name, age, address, creditCardNumber):
        self.name = name
        self.age = age
        self.address = address
        self.creditCardNumber = creditCardNumber
        self.cart = []

    def changeName(self, newName):
        self.name = newName
        print(f"New name: {self.name}")

    def changeAge(self, newAge):
        self.age = newAge
        print(f"New age: {self.age}")

    def changeAddress(self, newAddress):
        self.address = newAddress
        print(f"New address: {self.address}")

    def showCart(self):
        print(f"Cart: {self.cart}")

    def addProductToCart(self, productName, quantity):
        product = (productName, quantity)
        self.cart.append(product)
        print(f"Product {product} added successfully!")

    def removeProductFromCart(self, productName):
        removeProduct = False
        for i in range(len(self.cart)):
            if(self.cart[i][0] == productName):
                removeProduct = True
                break

        if removeProduct:
            self.cart.pop(i)
            print("Product removed successfully!")
        else:
            print("Product not found!")

    def buy(self):
        print(f"Products bought successfully with card: {self.creditCardNumber}")
        self.showCart()
        self.cart = []

    def __str__(self):
        return f"Name: {self.name} - Age: {self.age} - Address: {self.address} - Credit Card {self.creditCardNumber}"