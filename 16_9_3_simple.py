class Client:
    def __init__(self, firstname, lastname, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def printInformation(self):
        print('Клиент "{} {}".Баланс: {} руб.'.format(self.firstname, self.lastname, self.balance))

client_1 = Client("Иван", "Петров", "50")
client_1.printInformation()
