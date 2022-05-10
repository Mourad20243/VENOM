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
directions = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    (-1,  1),
    ( 1, -1),
    (-1, -1)
]



####
class GameEnd(Exception):
	def __init__(self, lastState):
		self.__state = lastState

	@property
	def state(self):
		return self.__state

	def __str__(self):
		return 'Game Over'
class GameDraw(GameEnd):
	def __init__(self, lastState):
		super().__init__(lastState)

	def __str__(self):
		return super().__str__() + ': Draw'


class BadMove(Exception):
	pass
def coord(index):
    return index // 8, index % 8

def index(coord):
    l, c = coord
    return l*8+c

def walk(start, direction):
    current = start
    while isInside(current):
        current = add(current, direction)
        yield current
def isInside(coord):
    l, c = coord
    return 0 <= l < 8 and 0 <= c < 8
def add(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return l1 + l2, c1 + c2





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

def possibleMoves(state):
    res = []
    for move in range(64):
        try:
            willBeTaken(state, move)
            res.append(move)
            print(res)
        except BadMove:
            pass
    return res

def willBeTaken(state, move):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    if not (0 <= move < 64):
        raise BadMove('Your must be between 0 inclusive and 64 exclusive')

    if move in state['board'][0] + state['board'][1]:
        raise BadMove('This case is not free')

    board = []
    for i in range(2):
        board.append(set((coord(index) for index in state['board'][i])))

    move = coord(move)

    cases = set()
    for direction in directions:
        mayBe = set()
        for case in walk(move, direction):
            if case in board[otherIndex]:
                mayBe.add(case)
            elif case in board[playerIndex]:
                cases |= mayBe
                break
            else:
                break

    if len(cases) == 0:
        raise BadMove('Your move must take opponent\'s pieces')
    
    return [index(case) for case in cases]
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
                    the_move_played = random.choice(possibleMoves(message["state"]))
                    client.send(json.dumps({"response": "move","move":the_move_played ,"message": "prouve le "}).encode())
                elif possibleMoves(message["state"])== []:
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