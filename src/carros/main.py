from frota import *

def operarcarro (carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1,2,3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    nm_consumo = float (input ('Digite o consumo médio:'))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, nm_consumo, 100)

    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    nm_consumo = float (input('Digite o consumo médio:'))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, nm_consumo, 100)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while (carro1.get_odometro() < 600 and carro2.get_odometro() < 600) and (carro1.get_tanque() > 0 or carro2.get_tanque() > 0):
        try:    
            op = 0
            while op not in (1,2):
                op = int (input ("qual carro vc quer mexer?"))
                if op == 1:
                    operarcarro(carro1)
                else:
                    operarcarro(carro2)
            print('Infos atuais do carro')
            print(carro1)
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    # carro1.desligar()
    # carro2.desligar()

    if carro1.get_odometro() > 600 or carro2.get_odometro() > 600:
        if op == 1:
            print ("O Carro 1 venceu!!!")
        else:
            print ("O Carro 2 venceu!!!")
    else:
        print ("os dois carros ficaram sem gasolina")

    try:
        with open ('carros.pkt', 'wb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print (e)
        

