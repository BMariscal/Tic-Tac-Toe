import random, sys

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}




def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    return 'This is the current board'






def check_winner():
	global Again
	if Again == True:

    
	    if theBoard['top-l'] == token and theBoard['top-m'] == token and theBoard['top-r'] == token:
		    print (token + ' wins!!!!')
		    again()
		    
	    elif theBoard['mid-l'] == token and theBoard['mid-m'] == token and theBoard['mid-r'] == token:
		    print (token + ' wins!!!!')
		    again()
		    
	    elif theBoard['low-l'] == token and theBoard['low-m'] == token and theBoard['low-r'] == token:
	        print (token + ' wins!!!!')
	        again()
	        
	    elif theBoard['top-l'] == token and theBoard['mid-l'] == token and theBoard['low-l'] == token:
	        print (token + ' wins!!!!')
	        again()
	       
	    elif theBoard['top-m'] == token and theBoard['mid-m'] == token and theBoard['low-m'] == token:
	        print (token + ' wins!!!!')
	        again()
	        
	    elif theBoard['top-r'] == token and theBoard['mid-r'] == token and theBoard['low-r'] == token:
	        print (token + ' wins!!!!')
	        again()
	        
	    elif theBoard['top-l'] == token and theBoard['mid-m'] == token and theBoard['low-r'] == token:
	        print (token + ' wins!!!!')
	        again()
	        
	    elif theBoard['top-r'] == token and theBoard['mid-m'] == token and theBoard['low-l'] == token:
	        print (token + ' wins!!!!')
	        again()
	    else:
	    	pass


def again():
	global theBoard, Again
	a=(input('Play again: Y or N :').lower())
	if a =='n':
		sys.exit()
	else:
		theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
		new()
		


def goes_first():
	global token
	start = (random.randint(0,2))
	if start == 0:
		token = 'X'
		print
		print('X starts the game')
		return token
	else:
		token ='O'
		print
		print('O starts the game')
		return token

def game_play():
	global theBoard, token, Again, pick
	for i in range(0,9):
	    pick = (input("""Enter your position. Your options are: 
	    	top-L, top-M, top-R, mid-L, mid-M, mid-R,low-L, low-M, low-R,
	                                    """).lower())
	    check_input()

	    
	    print(printBoard(theBoard))
	    if i >= 4:
	    	Again = True
	    	check_winner()
	    else:
	    	pass
	    if i == 8:
	    	print('No one wins')
	    	break

	    if token == 'X':
	        token = 'O'
	        print("It's now {0}'s turn".format(token))
	    else:
	        token = 'X'
	        print("It's now {0}'s turn".format(token)) 
	again()
	        

def new():
	Again = False        
	print("-----"*15)
	print("Welcome to Tic-Tac-Toe!")
	print(printBoard(theBoard))
	goes_first() 
	game_play()  



def check_input():
	global pick, theBoard, token
	if pick in theBoard:
		if theBoard[pick] == ' ':
			theBoard[pick] = token
		else:
			print(">>>Spot taken. Please pick another location next time<<<")
			#game_play()

	else:
		print(">>>Incorrect input. Please enter one of the options next time<<<")
		#game_play()



new()  
     

    