class A:
    def __init__(self):
        self.A1 = 0
        self.A2 = 0.0

    def MA1(self):
        print("Método MA1")

    def MA2(self):
        print("Método MA2")

    def MA3(self):
        print("Alteração a classe A partir do clone")

class B:
    def __init__(self):
        self.B1 = 0
        self.B2 = 0.0

    def MB1(self):
        print("Método MB1")

    def MB2(self):
        print("Método MB2")

    def MB3(self):
        print("Método MB3")

class C:
    def __init__(self):
        self.C1 = ""
        self.C2 = 0

    def MC1(self):
        print("Método MC1")

    def MC2(self):
        print("Método MC2")

    def MC3(self):
        print("Método MC3")
class D:
    def __init__(self, D1: str, D2: int):
        self.D1 = D1
        self.D2 = D2

    def MD1(self):
        print(f"Método MD1: {self.D1}")

    def MD2(self):
        print(f"Método MD2: {self.D2}")

#questao 28 solicitada alteração
