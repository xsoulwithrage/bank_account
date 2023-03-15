class CuentaBancaria:
    nombre_banco = "Ed Bank"
    todas_las_cuentas = []

    def __init__(self, numero_cuenta, tasa_interes, balance):
        self.numero_cuenta = numero_cuenta
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Sin fondos suficientes")
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print("Balance actual: ", self.balance)
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)  
        return self


    @classmethod
    def imprime_cuentas_bancarias(cls): 
        for account in cls.todas_las_cuentas:
            account.mostrar_info_cuenta()