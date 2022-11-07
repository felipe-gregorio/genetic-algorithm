import random

chanceMutacao = 10
listaGenes1 = ['N', 'L', 'S', 'O']
#[(N,20), (L, 10), (N, 5), (S ,15)]- exemplo

idGlobal = 0

class Coadjuvante:

    

    def __init__(self, x, y, genePai1 = None, genePai2 = None):
        global idGlobal
        self.id = idGlobal
        idGlobal = idGlobal + 1
        self.idade = 0
        self.x = x
        self.y = y
        self.gene1 = self.__geraGene1(genePai1, genePai2)

    def __geraGene1(self, genePai1, genePai2):
        gene = []
        if not genePai1 and not genePai2:
            for i in range(4):
                gene.append((random.choice(listaGenes1), random.randint(0, 150)))
        elif genePai1 and genePai2:
            gp1 = genePai1.gene1.copy()
            gp2 = genePai2.gene1.copy()
            #mutacaoDirec
            if random.randint(1, 100) <= chanceMutacao:
                utilTupla(gp1[0], 0, random.choice(listaGenes1))
                print('Houve Mutação no id ' + str(self.id))
            #mutacaoTama
            if random.randint(1, 100) <= chanceMutacao:
                utilTupla(gp1[0], 1, random.randint(0,150))
                print('Houve Mutação no id ' + str(self.id))
            gene.append(gp1[0])
            gene.append(gp1[1])
            gene.append(gp2[2])
            gene.append(gp2[3]) 
        return gene

    def printaGene1(self):
        print(self.gene1)

    def printaPosicao(self):
        print("ID" + str(self.id) + " X:" + str(self.x) + " - Y:" + str(self.y) + "| Idade: " + str(self.idade))
        


def utilTupla(tupla, pos, item):
    my_list = list(tupla)
    my_list[pos] = item
    return tuple(my_list)
