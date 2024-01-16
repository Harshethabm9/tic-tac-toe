# This function check and add names of the players

def getPlayerNames():
    while True:
        player1 = input("Enter the name of 1st Player: ").strip()
        player2 = input("Enter the name of 2nd Player: ").strip()

        if player1 != "" and player2 != "" and player1 != player2:
            return player1, player2
        else:
            print("Invalid names. Names cannot be empty or the same. Please try again.")
