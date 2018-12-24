import random
class jogo:
    def __init__(self):
        self.forca = open('forca.txt','r')
        self.a = self.forca.readlines() #li a palavra
        self.c = random.randint(0,len(self.a)-4) 
        self.d = self.a[self.c] #acessei um termo aleatorio da minha lista
        self.n = 0
        self.m = 0
        self.lista = [] #armazendo as letras que o usuário já colocou
        self.correto = [] #letras corretas
        self.erro = [] #letras erradas
        
    def efetuar(self):
        aaa = []
        for i in range(0,len(self.d)-1):
            aaa.append('-')
        while True:
            if self.n == 0:
                print('  ______')
                print(' |      |')
                print('        |')
                print('        |')
                print('        |')
                print('        |')
                print('        |')
            elif self.n == 1:
                print('  ______')
                print(' |      |')
                print(' O      |')
                print('        |')
                print('        |')
                print('        |')
                print('        |')
            elif self.n == 2:
                print('  ______')
                print(' |      |')
                print(' O      |')
                print(' |      |')
                print(' |      |')
                print('        |')
                print('        |')
            elif self.n == 3:
                print('  ______')
                print(' |      |')
                print(' O      |')
                print('/|      |')
                print(' |      |')
                print('        |')
                print('        |')
            elif self.n == 4:
                print('  ______')
                print(' |      |')
                print(' O      |')
                print('/|\     |')
                print(' |      |')
                print('        |')
                print('        |')
            elif self.n == 5:
                print('  ______')
                print(' |      |')
                print(' O      |')
                print('/|\     |')
                print(' |      |')
                print('/       |')
                print('        |')
            
            print(''.join(aaa))
            k = str(input('Qual letra: '))
            x = k.lower()
            if x in self.lista:
                print('Letra repetida! Tente novamente')
            elif len(x)>1:
                print('Não seja trapaceiro! Uma letra de cada vez!')
            elif x in self.d:
                print('Letra correta')
                self.correto.append(x)
                self.m = self.m + self.d.count(x)
                for i in range(0,len(self.d)-1):
                    if x == self.d[i]:
                        aaa[i] = x
            else:
                self.erro.append(x)
                print('Você errou')
                self.n = self.n + 1
                
            self.lista.append(x)
            if self.n>=6:
                print('Você perdeu')
                print('  ______')
                print(' |      |')
                print(' O      |')
                print('/|\     |')
                print(' |      |')
                print('/ \     |')
                print('        |')
                print('Palavra correta: ',self.d)
                break
            if self.m == len(self.d)-1:
                print('Parabens, você ganhou!')
                print('Palavra correta: ',self.d)
                break
            print('Letras corretas: ','-'.join(self.correto))
            print('Letras erradas: ','-'.join(self.erro))
tent = jogo()
tent.efetuar()





        
    


    

