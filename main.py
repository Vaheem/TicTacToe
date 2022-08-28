import numpy as np
#import tkinter

#root = tkinter.Tk()
#tkinter.Label(root)
#root.mainloop()

def game(numer_of_steps, pos_list, game_field, game_not_over):
    cur_player = numer_of_steps % 2

    if cur_player == 1:
        game_field[pos_list[0], pos_list[1]] = 1
    else:
        game_field[pos_list[0], pos_list[1]] = 2

    print(game_field)
    #At least 5 steps shold be played so it is possible that one of the players wins
    if numer_of_steps > 4:
        if np.prod(game_field[0]) == 1 or np.prod(game_field[1]) == 1 or np.prod(game_field[2]) == 1\
                or np.prod(game_field.diagonal()) == 1 or np.prod(np.fliplr(game_field).diagonal()) == 1\
                or np.prod(game_field[:, 0]) == 1 or np.prod(game_field[:, 1]) == 1 or np.prod(game_field[:, 2]) == 1:

            print("Player 1 won")
            game_not_over[0] = False
            return game_not_over
        elif np.prod(game_field[0]) == 8 or np.prod(game_field[1]) == 8 or np.prod(game_field[2]) == 8 \
                or np.prod(game_field.diagonal()) == 8 or np.prod(np.fliplr(game_field).diagonal()) == 8 \
                or np.prod(game_field[:, 0]) == 8 or np.prod(game_field[:, 1]) == 8 or np.prod(game_field[:, 2]) == 8:
            print("Player 2 has won")
            game_not_over[0] = False





def main():
    #Creating an empty numpy array
    game_field = np.zeros([3,3], dtype=int)
    game_not_over = [True]
    number_of_steps = 0
    #While the game is not over ask the player a position
    while(game_not_over[0]):
        if number_of_steps > 8 and game_not_over[0]:
            print("DRAW")
            break
        else:
            #The user input has the type string E.G. 1, 2
            position_str = input("Enter position:")
            pos_list = [int(x) for x in position_str.split(",")]
            for entry in pos_list:
                if entry > 2 or entry < 0:
                    print("Wrong input type")
                    print("Game Over")
                    game_not_over[0] = False
            if not game_not_over:
                break
            number_of_steps = number_of_steps + 1
            game(number_of_steps, pos_list, game_field, game_not_over)













if __name__ == "__main__":
    main()