import random

board = []

for i in range(0,5):
  board.append(["o"] * 5)

for row in board:
    print (" ".join(row))
print("Let's play!")
print("This is a 2 player game")

player_1 = input("Enter first name: ")
player_2 = input("Enter second name: ")
players = [player_1, player_2]

for i in range(0,5):
  row = random.randint(0,len(board)-1)
  col = random.randint(0,len(board[0])-1)
  print(" ".join(board[i]))

if random.choice(players) == player_1:
  print(player_1, "starts the game.")
else:
  print(player_2, "starts the game.")

ship_row_1 = random.randint(0,len(board)-1)
ship_col_1 = random.randint(0,len(board[0])-1)

ship_row_2 = random.randint(0,len(board)-1)
ship_col_2 = random.randint(0,len(board[0])-1)

for i in range(5):
  print(" ".join(board[i]))

player_start = random.choice(players)

hit_count = 0

for turn in range(4):
     guess_row = int(input("Guess Row: (allowed values: 0-4) "))
     guess_col = int(input("Guess Col: (allowed values: 0-4) "))

     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("Congratulations! ")
            if hit_count == 1:
                   print("You sunk first battleship!") 
            elif hit_count == 2:
                   print("You sunk second battleship! You win!")
                   print(" ".join(board[5]))
                   break
     else:
            if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
                   print ("Oops, you miss the board.")
            elif(board[guess_row][guess_col] == "X"):
                   print ("You guessed that one already.")
            else:
                 print ("You missed my battleship!")
                 board[guess_row][guess_col] = "X"
            print (turn + 1, "turn")
     for i in range(5):      
      print(" ".join(board[i]))
print ("Ship 1 is hidden:")    
print (ship_row_1)
print (ship_col_1)

print ("Ship 2 is hidden:")    
print (ship_row_2)
print (ship_col_2)