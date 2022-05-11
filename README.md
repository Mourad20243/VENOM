# VENOM

# projet d'informatique Othello chafik adel , Mourad Aarab 

ce projet consiste en la realisation d'une intelligence artificielle(IA) pour le jeu Othello.
Notre IA qui sera le client devra interagir avec le serveur pour pouvoir se connecter.
Cela nous permettra d'échanger des informations avec le serveur afin de respecter certaine condition pour demarrer le championnat . 
## Stratégie utilisée
notre projet se base sur une fonction :  
    -bestcoup()
cette fonction permet de jouer les meilleurs coups possibles face a une IA random. 
le principe est simple lorsque le serveur nous envoie une requette de certaines cases de possibilité a jouer , la fonction selectionnera les cases censé etre les mieux joues (via la fonction possibleMove). 

les meilleures cases sont principalement les coins(bestcoup). 
la fonction bestcoup renvoie du meilleur coup possible a jouer au pire coup cad que si aucun meilleur coup est a jouer il devra etre obliger de joue un coup pas tres utile . 


## Listes des requêtes / réponse : 

### Inscription : 

Afin de pouvoir jouer, le client doit s'inscrire sur celui-ci. Pour cela, il doit envoyer un message sous format Json au serveur contenant ses données, en communiquant au serveur qui se trouve sur le port 3000.

Contenu du message : 

```json
{
"request": "subscribe",
"port": port,
"name": name,
"matricules": ["20132", "20104"]
}
```



Si tout se passe correctement, le serveur répond : 

```json
{
   "response": "ok"
}
```


### Vérification de la présence : 


 Afin de vérifier si le client est toujours connecté, le serveur envoit régulièrement des requète "ping" sur le port mentionné lors de l'inscription, auquelle nous devons répondre "pong"

Requète ping : 

```json
{
   "request": "ping"
}
```
Réponse : 

```json
{
   "response": "pong"
}
```
réponse en cas d'erreur:
```json
{
   "response": "error",
   "error": "error message"
}
```json
### Requête de coup : 



Lorsque c'est au tour du joueur de donner son coup, le serveur envoit une requête play au client qui devra renvoyer son coup .


Requête play du serveur : 

```json
{
   "request": "play",
   "lives": 3,
   "errors": list_of_errors,
   "state": state_of_the_game
}
```

La variable lives donne le nombre de vies restantes du joueur, chaque joueur a 3 vies par match et en perd une à chaque mauvais mouvement effectué. Si le nombre de vies tombe à 0, le joueur perd.

La variable errors liste les raisons pour lesquelles les coups joués étaient mauvais.

La variable state donne l'état du jeu, elle contient différentes infos nécéssaire au client afin qu'il puisse décider comment jouer. 

La réponse du client est: 

```json
{
   "response": "move",
   "move": the_move_played,
   "message": "Fun message"
}

La variable Players donne les noms des joueurs inscris au match, le premier joueur représente celui qui joueura en premier avec les pions noirs. 

La variable current donne l'indice dans la liste Players du joueur devant donner son coup.

La variable board donne le plateau de jeu. 
