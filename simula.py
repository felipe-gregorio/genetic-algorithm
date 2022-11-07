
import Coadjuvante as cd

import random



cmax = 10



coadjs = []



for i in range(cmax):

    coadjs.append(cd.Coadjuvante(random.randint(-600, 600), random.randint(-600,600)))

    coadjs[i].printaPosicao()



for ger in range(10):

    # fazer o gene afetar o comportamento

    for coad in coadjs:

        for i in range(4):

            if coad.gene1[i][0] == 'N':

                coad.y = coad.y + coad.gene1[i][1]

            elif coad.gene1[i][0] == 'L':

                coad.x = coad.x + coad.gene1[i][1]

            elif coad.gene1[i][0] == 'S':

                coad.y = coad.y - coad.gene1[i][1]

            elif coad.gene1[i][0] == 'O':

                coad.x = coad.x - coad.gene1[i][1]

        coad.idade = coad.idade + 1

    # fazer o critério de seleção (matar == tirar da lista)

    for coad in coadjs:

        if coad.x < 0 or coad.y < 0:

            coadjs.remove(coad)

    # reproduzir os sobreviventes

    if len(coadjs) < 2:

        print('População não consegue mais se reproduzir')

        break

    for k in range(0, len(coadjs), 2):

        coadjs.append(cd.Coadjuvante(random.randint(-600, 600), random.randint(-600,600) , coadjs[k], coadjs[k+1]))

    # mostra a posicao final

    print("Geração " + str(ger))

    for coad in coadjs:

        coad.printaPosicao()

        coad.printaGene1()