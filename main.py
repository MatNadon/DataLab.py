import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

class Data():
    def __init__(self, path):
        #ouvre le fichier d'intéret
        with open(path, 'r') as fichier:
            self.content = fichier.readlines()

        #extrait les données du fichier txt
        self.data = []
        for line in self.content[24:]:
            self.data.append(line.split()) 
        #transforme la série de donnée en [[première série], [deuxième série], ...]
        self.data = list(map(list, zip(*self.data)))
        
        #transforme les éléments de la liste str en float
        self.data = [[float(x.replace(',','.')) for x in sublist] for sublist in self.data]

        self.channels = len(self.data)

    def __str__(self):
        txt = '1ere série:\n----------------------------------------------\n'
        for i in range(self.channels):
            txt += f'{self.data[i]}\n'
            if i+1 != self.channels:
                txt += f'\n\n{i+2}e série:\n----------------------------------------------\n'
        return txt
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __setitem__(self, idx, item):
        self.data[idx] = item

    def __delitem__(self, idx):
        del self.data[idx]
    
    def __len__(self):
        return len(self.data)
    
    def arrangeData(self):
        '''
        Permet de créer les arrays appropriées pour créer un graphique
        '''

        X = np.linspace(0, len(self.data[0])-1, len(self.data[0]))
        return X, self.data

    def plotData(self, data, titre, titreX, titreY):
        '''
        Créer un tableau de la série désiré
        '''
        X, Y = self.arrangeData()
        plt.plot(X, data)
        plt.title(titre)
        plt.xlabel(titreX)
        plt.ylabel(titreY)
        plt.grid()
        plt.show()

    def toExcel(self, titre):
        '''
        Transfère les données dans un fichier excel
        '''
        columns = []
        for i in range(self.channels):
            columns.append(f'Série {i}')
        df = pd.DataFrame(np.transpose(self.data))
        df.to_excel(f'{titre}.xlsx', index=False)


'''Exemple d'utilisation:'''
# donnée = Data("C:/Users/nadon/Downloads\données 2025-01-21-1.lvm")
# print(donnée)
# donnée.toExcel('Nom de fichier')
# X, Y = donnée.arrangeData()
# plt.plot(X, Y[0])
# donnée.plotData(Y[0], 'Axe des X', 'Axe des Y')

if __name__ == '__main__':
    '''
    Insérez votre code ici pour extraire les données!
    '''
