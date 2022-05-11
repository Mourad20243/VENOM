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
        print(elem)
        # if elem == 44 :
        #     best_move = elem 
        #     return best_move
        # else :
        #     return None
        if elem == 0 or elem == 7 or elem == 56 or elem == 63 :
            best_move = elem
            return best_move
        elif  elem == 2 or elem == 3 or elem == 4 or elem == 5 or elem == 23 or elem == 31 or elem == 39 or elem == 47 or elem == 61 or elem == 60 or elem == 59 or elem == 58 or elem == 40 or elem == 32 or elem == 24 or elem == 16:
            best_move = elem
            return best_move
        elif elem == 18 or elem == 21 or elem == 42 or elem == 45 or elem == 27 or elem == 28 or elem == 35 or elem == 36:
            best_move = elem
            return best_move   
        elif elem == 19 or elem == 20 or elem == 29 or elem == 37 or elem == 44 or elem == 43 or elem == 34 or elem == 26 :
            best_move = elem 
            return best_move
        elif elem == 10 or elem == 11 or elem == 12 or elem == 13 or elem == 22 or elem == 30 or elem == 38 or elem == 46 or elem == 53 or elem == 52 or elem == 51 or elem == 50 or elem == 41 or elem == 33 or elem == 25 or elem == 17 :
            best_move = elem 
            return best_move 
        elif elem == 1 or elem == 8 or elem == 6 or elem == 15 or elem == 55 or elem == 62 or elem == 48 or elem == 57:
            best_move = elem 
            return best_move 
        elif elem == 9 or elem == 14 or elem == 49 or elem == 54 :
            best_move = elem
            return best_move
        # else : 
        #     best_move = elem 
        #     return random.choice(list_coup)





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
                #print(message) 
                message1=str('{"response": "pong"}')
                if message =={"request": "ping"}: 
                    client.send(message1.encode())
                elif message['request'] == "play":
                    the_move_played = bestcoup(game.possibleMoves(message["state"]))
                    client.send(json.dumps({"response": "move","move":the_move_played ,"message": "siuuuuuu "}).encode())
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