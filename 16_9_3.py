class Client:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = 0 # изначально баланс неизвестен

    def setBalance(self, value):
        self.balance = value

    def printInformation(self):
        print('Клиент "{} {}".Баланс: {} руб.'.format(self.firstname, self.lastname, self.balance))

client_1 = Client("Иван", "Петров")
client_1.setBalance(50)
client_1.printInformation()

