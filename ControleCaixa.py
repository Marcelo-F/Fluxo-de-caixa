class ControleCaixa:
    from time import sleep
    
    # CONSTRUTOR
    def __init__(self):
        self.valor = []
        self.cadastro = [] 
        self.contasreceber = []
        self.receber = []
       
        self.somaganhos = 0
        self.somadivida = 0
        self.contas_a_pagar
        self.contas_a_receber

    # FUNÇÃO DO MENU
    def menu(self):
        print("---------------------------- |")
        print("             MENU            |")
        print("                             |")
        print("(1)  - [ Contas a pagar  ]   |")
        print("(2)  - [ Contas a receber]   |")
        print("(3)  - [ Extrato]            |")
        print("(4)  - [ Exit]               |")
        print("---------------------------- |")

        selection = int(input("OPÇÃO : "))

        if (selection == 1):
            self.contas_a_pagar()

        elif (selection == 2):
            self.contas_a_receber()

        elif (selection ==3):
            self.Extrato()
            

        elif  selection == 4: 
                exit
        else:
            print(" INFORME UMA OPÇÃO VALIDA ! ")
            self.sleep(1)
            return self.menu()
        
    # 1 - FUNÇÃO PARA O CADASTRO DE CONTAS
    def contas_a_pagar(self):
        print("-------------------------------------------------- |")
        print("               CONTAS A PAGAR                      |")
        print("                                                   |")
        print(" (1) - CADASTRAR CONTA | (2) - VOLTAR PARA O MENU  |")
        print("-------------------------------------------------- |")
         

        selection =  int(input(" OPÇÃO : "))

        if (selection == 1):
           # while (selection == 1):
                
                self.cadastro.append(input('Informe a sua divida : '))
                self.valor.append(float(input('Infome o valor da divida : ')))
                #for i in range (len(self.valor)):
                self.somadivida = sum(self.valor)
                   # self.somadivida += self.valor[i]
                print('O valor total da divida é: {}'.format(self.somadivida))
                return self.contas_a_pagar()
        elif(selection == 2):
            return self.menu()
        else:
            print(" INFORME UMA OPÇÃO VALIDA ! ")
            self.sleep(2)

    # 2 - VALORES A RECEBER
    def contas_a_receber(self): 
        print("-------------------------------------------------- |")
        print("               CONTAS A RECEBER                    |")
        print("                                                   |")
        print(" (1) - CADASTRAR GANHO | (2) - VOLTAR PARA O MENU  |")
        print("-------------------------------------------------- |")
        #colocar a variavel do calculo de saldo 

        selection =  float(input(" OPÇÃO : "))

        if selection == 1:
           # while (selection == 1):
                self.contasreceber.append(input('informe o seu ganho : '))
                self.receber.append(float(input('Valor do ganho : ')))
                self.somaganhos = sum(self.receber)
                print('O valor total dos ganhos é: {}'.format(self.somaganhos))
                return self.contas_a_receber()
        elif(selection == 2):   
            return self.menu()
        else:
            print(" INFORME UMA OÇÃO VALIDA ! ")
            self.sleep(2)

    # 3 - EXTRATO
    def Extrato(self):
        print()
        print("CONTAS A PAGAR")
        print(f'As suas contas são: {self.cadastro} \n')
        print(f"No valor          : {self.valor}\n") 
        print('Valor total a pagar: '+str(self.somadivida))
        print("--------------------------------------------")
        print()
        print("CONTAS A RECEBER")
        print()
        print(f'Contas a receber  :{self.contasreceber}\n')
        print(f'Ganhos            : {self.receber}\n')
        print('Valor total a receber:' +str(self.somaganhos))
        print()
        if self.somaganhos < self.somadivida:
            calculo = self.somaganhos - self.somadivida
            print("Sua empresa esta tendo perdas, se atentar. " + str (calculo))

        elif self.somaganhos == self.somadivida: 
            calculo = self.somaganhos - self.somadivida
            print("Tomar cuidado os seus ganhos e perdas foram bem equilibrado" +str(calculo))
        else: 
            calculo = self.somaganhos - self.somadivida
            print("Esta tendo mais ganho do que gasto, continue assim !!" +str(calculo))
   