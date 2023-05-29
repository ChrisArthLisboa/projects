
v = float(input("Qual é a velocidade atual do carro: "))
if v > 80:
    print(f"\033[0;31mMULTADO! Você excedeu o limite de velocidade permitido que é 80 Km/h. \nVocê deve pagar uma multa\033[0;37m de \033[1;31mR${(v -80)*7:.2f}\033[0;37")
print("\033[0;32mTenha um bom dia! Dirija com segurança!\033[0;37m")
