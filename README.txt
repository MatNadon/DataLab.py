S'IL Y A DES BUGS, INFORMEZ MOI. JE VAIS ESSAYER DE LES RÉSOUDRE ---> (Matis Nadon, manad277@ulaval.ca)

Veuillez vous assurez d'avoir importé tous les Packages nécessaire incluant 'openpyxl' (pour EXCEL)

Bonjour, ce code rudimentaire permet d'extraire les données des fichiers de lab du cours Électronique et mesures expérimentale.
Pour l'utiliser, il faut simplement initialisé un objet Data avec le chemin d'accès du fichier d'intérêt.

Exemple de chemin d'accès:
"C:/Users/nadon/Downloads\données 2025-01-21-4.lvm"

Attention aux \ qui peuvent être considéré par Python comme un modificateur de string. Remplacer le caractère par un / si celui-ci créer des soucis.

La classe organise les données dans le bon ordre de mesures (Channels). Je vous invite à print() un objet de la classe pour les examiner.
Pour sélectionner une certaine série de données, il suffit d'utiliser un indice: donnée[0], donnée[1], etc.

Pour mieux utiliser le code, vous rapidement lire les différentes méthodes. C'est rien de trop gros.

arrangeData():
Fonction qui permet de créer les arrays nécessaire pour faire un graphique. À utiliser si vous voulez faire vos propres style de graph. Voir https://matplotlib.org/stable/users/index

plotData(idx):
    -idx est l'indice de la série dans l'objet (donnée[1]). Il est par défaut à 0.
C'est une version extrêmement élémentaire pour 'Plot' un graphique. 
Je vous conseille de le faire vous même dans le Main tout en bas, car chaque graphique à besoin de son propre style!

toExcel(titre):
    -nom du fichier
Pour ceux qui préfère faire leur graph dans Excel, vous n'êtes pas oublié! Vous pouvez utiliser cette méthode qui va créer un fichier excel avec les données dans le meme répertoire que le code.

__méthode__():
Toutes les méthodes qui, selon moi, sont intéressantes pour cette classe ont été implémenté. Vous pouvez donc modifier, ajouté et supprimé des données!