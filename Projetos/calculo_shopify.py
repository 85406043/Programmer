#Shop calculator
import os

# Preço final + (Valor do Droplatam + 25000) x 1,5 =
def calculo_shop():
    while True:
        delete();global provedor
        provedor = float(input('Digite o valor do Produto(Provedor Latam) = COP $'))
        calc = (provedor + 25000) * 1.5
        print(f'Valor reajustado: \nCOP $\033[32m{calc}\033[m')
        print(25*'=-')
        confirm = input('Ir para o calculo de margem de lucro?[Y/N]').strip().capitalize();delete()
        if confirm == 'Y':
            margem_lucro()
        else:
            pass
        
#Function delete
def delete():
    os.system('clear')
#Shop Margem Lucro %

# Formula: Margem % = (Lucro ÷ Preço Final) × 100
#       = (21.300 ÷ 63.900) × 100 ≈ 33,3%
def margem_lucro():
    while True:
        delete();global provedor
        number = float(input('Informe o valor do produto reajustado: COP $'))
        print(25*'=-')
        lucro = (number - 25000) - provedor
        margem = (lucro / number) * 100
        print(f'A margem de lucro, retirando COP $25000: \n \033[32m%{margem:.2f}\033[m')
        print(25*'=-')
        interrog = input('Deseja sair da Margem de Lucro?[Y/N]').strip().capitalize();delete()
        if interrog == 'Y':
            calculo_shop()
        else:
            pass

calculo_shop()