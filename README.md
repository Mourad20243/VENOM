# VENOM

projet d'informatique Othello chafik adel , Mourad Aarab 

ce projet consiste en la realisation d'une intelligence artificielle(IA) pour le jeu Othello.
Notre IA qui sera le client devra interagir avec le serveur pour pouvoir se connecter.
cela nous permettra d'échanger des informations avec le serveur afin de respecter certaine condition pour demarrer le championnat . 

notre projet se base sur une fonction :  
    -bestcoup()
cette fonction permet de jouer les meilleurs coups possibles face a une IA random. 
le principe est simple lorsque le serveur nous reponds certaines cases de possibilité a jouer , la fonction selectionnera les cases censé etre les mieux joues (via la fonction possibleMove). 

les meilleurs cases sont principalement les coins(bestcoup) . 
