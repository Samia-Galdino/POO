class Cachorro:
    def __init__(self, nome, idade, raca, comida, energia=100):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = True
        self.energia = energia
    
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} acordou!")
    
    def dormir(self):
        self.acordado = False
        self.energia = 100
        print(f"{self.nome} foi dormir e recuperou sua energia.")
    
    def comer(self):
        if self.acordado:
            print(f"{self.nome} está comendo {self.comida}.")
            self.energia += 10
        else:
            print(f"{self.nome} está dormindo e não pode comer agora.")
    
    def brincar(self):
        if self.acordado and self.energia > 10:
            print(f"{self.nome} está brincando e está muito feliz!")
            self.energia -= 10
        else:
            print(f"{self.nome} está cansado ou dormindo, não pode brincar agora.")
    
    def status(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Raça: {self.raca}, Energia: {self.energia}, Feliz: {self.feliz}")

# Criando um cachorro
cachorro1 = Cachorro(nome="Dom", idade=1, raca="Pitbull", comida="ração")

# Testando os comandos
cachorro1.acordar()
cachorro1.comer()
cachorro1.brincar()
cachorro1.dormir()
cachorro1.status()