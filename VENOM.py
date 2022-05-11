import json
import socket
import time
import threading
import sys
import random
import game

# from PI2CChampionshipRunner.games.othello import game

# from PI2CChampionshipRunner.games import othello

# moves = possibleMoves(state)
# move = random.choice(moves)





address = ('localhost', 3000)
serveurAddress = ("0.0.0.0" , 8888)
def sender():
        
        with socket.socket() as s:
            s.connect(address)
            message = json.dumps({
    "request": "subscribe",
    "port": 8888,
    "name": "VENOM",
    "matricules": ["12345", "0000"]
 }

            )

            s.send(message.encode())
            print(s.recv(2048).decode())

def bestcoup(list_coup):
    best_move = None#random.choice(list_coup)
    for elem in list_coup:
        if elem == 0 or elem == 7 or elem == 56 or elem == 63 :
            best_move = elem
            return best_move
        elif elem == 1 or elem == 2 or elem == 3 or elem == 4 or elem == 5 or elem == 6 or elem == 8 or elem == 16 or elem == 24 or elem == 32 or elem == 40 or elem == 48 or elem == 57 or elem == 58 or elem == 59 or elem == 60 or elem == 61 or elem == 62 or elem == 15 or elem == 23 or elem == 31 or elem == 39 or elem == 47 or elem == 55:

            best_move = elem
            return best_move
        elif elem == 9 or elem == 14 or elem == 49 or elem == 54:
            best_move = None
            return best_move

        else :
            best_move = random.choice(list_coup)
            return best_move




# def random():
#     i = game.possibleMoves(a)
#     a = random.choice(i)
#     return 

def receiv():
    with socket.socket() as s : 
        s.bind(serveurAddress)
        s.listen()
        while True :
            client , address = s.accept()
            with client :
                message = json.loads(client.recv(2048).decode())
                print(message) 
                message1=str('{"response": "pong"}')
                if message =={"request": "ping"}: 
                    client.send(message1.encode())
                elif message['request'] == "play":
                    the_move_played = bestcoup(game.possibleMoves(message["state"]))
                    client.send(json.dumps({"response": "move","move":the_move_played ,"message": "prouve le "}).encode())
                elif game.possibleMoves(message["state"])== []:
                    the_move_played = None

                
                        


#thread = threading.Thread(target=sender, daemon=True)
#thread.start()

sender()
receiv()

    # response = s.recv(2048).decode()


# def hello():
#     while True:
#         time.sleep(1)
#         print('hello')
# thread = threading.Thread(target=hello, daemon=True)
# thread.start()
# while True:
#     time.sleep(1)
#     print('bye')



# print(response)


# liste_possible= [15, 7, 19 , 44 ]

# print(bestcoup(liste_possible))