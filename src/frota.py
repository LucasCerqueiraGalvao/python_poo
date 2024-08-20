class Carro:
    modelo : str
    marca : str
    cor : str
    consumo_medio: float
    odometro : float = 0
    tanque : float = 100
    motor_on : False

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, consumo: float, tanque:float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.consumo_medio = consumo
        self.tanque = tanque
        self.motor_on = motor

    def ligar(self):
        if not self.motor_on:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:

            
            self.tanque -= (velocidade * tempo)/(self.consumo_medio)

            if self.tanque >= 0:
                self.odometro += velocidade * tempo
            else:
                self.odometro += velocidade * tempo + (self.consumo_medio * self.tanque) 
                self.tanque = 0
                print ("Carro sem gasolina!!!")

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}')
        return info



