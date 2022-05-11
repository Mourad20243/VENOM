import json
import socket
import time
import threading
import sys
import random


import game


address = ('localhost', 3000)
serveurAddress = ("0.0.0.0" , 8880)



def sender():
        
        with socket.socket() as s:
            s.connect(address)
            message = json.dumps({
    "request": "subscribe",
    "port": 8888,
    "name": "SPIDERMAN",
    "matricules": ["54321", "9999"]
 }

            )

            s.send(message.encode())
            print(s.recv(2048).decode())

def receiv():
    with socket.socket() as s : 
        s.bind(serveurAddress)
        s.listen()
        while True :
            client , address = s.accept()
            with client :
                message = json.loads(client.recv(2048).decode())
                message1=str('{"response": "pong"}')
                if message =={"request": "ping"}: 
                    client.send(message1.encode())
                elif message['request'] == "play":
                    try : 

                        the_move_played = random.choice(game.possibleMoves(message["state"]))
                        client.send(json.dumps({"response": "move","move":the_move_played }).encode())
                    except : 
                        the_move_played = None
                        client.send(json.dumps({"response": "move","move":the_move_played }).encode())


sender()
receiv()