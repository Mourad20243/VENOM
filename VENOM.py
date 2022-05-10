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
    "port": 4096,
    "name": "VENOM",
    "matricules": ["12345", "0000"]
 }

            )

            s.send(message.encode())
            print(s.recv(2048).decode())

# def bestcoup(list_coup):
#     best_move = random.choice(list_coup)
#     for elem in list_coup:
#         if elem == 0 :#or elem == 7 or elem == 56 or elem == 63:
#             best_move = elem
#         return best_move



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
                    the_move_played = random.choice(game.possibleMoves(message["state"]))
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