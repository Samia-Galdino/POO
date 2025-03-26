class Carro:
    def __init__(self, modelo, ano, cor, combustivel=0, limite_velocidade=200):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0
        self.limite_velocidade = 200
    
    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print("Carro ligado.")
        else:
            print("Sem combustível para ligar o carro!")
    
    def desligar(self):
        self.ligado = False
        self.velocidade = 0
        print("Carro desligado.")
    
    def acelerar(self, incremento):
        if self.ligado:
            if self.velocidade + incremento <= self.limite_velocidade:
                self.velocidade += incremento
                print(f"Acelerando para {self.velocidade} km/h.")
            else:
                self.velocidade = self.limite_velocidade
                print(f"Velocidade máxima atingida: {self.limite_velocidade} km/h.")
        else:
            print("Ligue o carro antes de acelerar!")
    
    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
            print(f"Freando para {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print("O carro parou.")
    
    def abastecer(self, quantidade):
        self.combustivel += quantidade
        print(f"Abastecido com {quantidade} litros. Combustível atual: {self.combustivel} litros.")

# Criando um carro
carro1 = Carro(modelo="Oroch", ano=2018, cor="Prata")

# Testando os comandos
carro1.abastecer(10)
carro1.ligar()
carro1.acelerar(50)
carro1.frear(20)
carro1.desligar()
