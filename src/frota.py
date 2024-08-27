class Carro:
    modelo : str
    marca : str
    cor : str
    consumo_medio: float
    __odometro : float = 0
    __tanque : float = 100
    __motor_on : False

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, consumo: float, tanque:float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.consumo_medio = consumo
        self.__tanque = tanque
        self.__motor_on = motor

    def ligar(self):
        if not self.__motor_on:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:

            
            self.__tanque -= (velocidade * tempo)/(self.consumo_medio)

            if self.__tanque >= 0:
                self.__odometro += velocidade * tempo
            else:
                self.__odometro += velocidade * tempo + (self.consumo_medio * self.__tanque) 
                self.__tanque = 0
                print ("Carro sem gasolina!!!")

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}')
        return info
    
    def __repr__(self):
        info = (f'Carro (modelo = "{self.modelo}", marca = "{self.marca}", '
                f'cor = "{self.cor}", odometro = \n{self.__odometro}, '
                f'motor_on = {self.__motor_on}, '
                f'tanque = {self.__tanque}, '
                f'consumo_medio = {self.consumo_medio}')
        return info
    
    def get_odometro(self):
        return self.__odometro
    
    def get_tanque(self):
        return self.__tanque
    
    def get_motor(self):
        return self.__motor_on



