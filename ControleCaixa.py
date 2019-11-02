class ControleCaixa:
    def __init__(self):
        self.valor = []
        self.cadastro= [] 
        self.contasreceber = 0
        self.receber = 0
        self.n = 'n'
       
        self.somaganhos=0
        self.somadivida=0
        self.contas_a_pagar
        self.contas_a_receber
#1-contas a pagar
    def contas_a_pagar(self):
        print('CONTAS A PAGAR')
        self.n=input('Quer informar outra conta a pagar? \n')
        while (self.n != 'n'):
            self.cadastro.append = (input('informe a sua divida: '))
            self.valor.append = float(input('Infome o valor da divida:'))
            self.somadivida = self.somadivida + self.valor
            self.n=input('Quer informar outra conta a pagar? \n')
            print(f'As suas contas são: {self.cadastro} \n')
            print(f"No valor          :. {self.valor}\n")
# 2- contas a receber
    def contas_a_receber(self): 
        print('CONTAS A RECEBER')
        n=input('Cadastrar  conta a receber  ? s para sim a ou n para sairmos')
        while (n != 'n'):
            self.contasreceber.append=(input('informe o seu ganho: '))
            self.receber.append=(float(input('Valor do ganho: ')))
            self.somaganhos = self.somaganhos + self.receber
            n=input('Outro ganho para receber ? s para sim a ou n para sairmos')
#3-Extrato
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
