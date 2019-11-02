from ControleCaixa import ControleCaixa
controle = ControleCaixa()

print("---------------------------- |")
print("             MENU            |")
print("                             |")
print("(1)  - [ Contas a pagar  ]   |")
print("(2)  - [ Contas a receber]   |")
print("(3)  - [ Extrato]            |")
print("(4)  - [ Exit]               |")
print("---------------------------- |")

selection = int(input("OPÇÃO : "))

if selection == 1:
    controle.contas_a_pagar()

elif selection == 2:
    controle.contas_a_receber()

elif selection ==3:
    controle.Extrato()
    

elif  selection == 4: 
        exit
