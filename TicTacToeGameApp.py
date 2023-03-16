from TicTacToeClass import *
def main():
    response = ""
    while response != "No":
        size = input("Enter the size of board game. \n")
        print("\nSize of board game is " + size + "\n")
        searchStrategyO = input("Enter random, alpha, or minimax legal moves search strategy for O. \n")
        searchStrategyX = input("Enter random, alpha, or minimax legal moves search strategy for X. \n")

        print("\nSearch strategy for O is " + searchStrategyO + "\n")
        print("\nSearch strategy for X is " + searchStrategyX + "\n")

        game = TicTacToe(int(size), int(size), 3)
        # game = TicTacToe(int(size), int(size), int(size))
        print("Search strategy for play X is: " + searchStrategyX)
        print("Search strategy for play O is: " + searchStrategyO)
        # def game(self, searchStrategyX, searchStrategyO):

        """ Prof. Ben's Update """

        if searchStrategyX == "random" and searchStrategyO == "random":
            print(play_game(game, dict(X=random_player, O=random_player), verbose=True).utility)
        if searchStrategyX == "minimax" and searchStrategyO == "minimax":
            print(play_game(game, dict(X=player(minimax_search), O=player(minimax_search)), verbose=True).utility)
        if searchStrategyX == "alpha" and searchStrategyO == "alpha":
            print(play_game(game, dict(X=player(alphabeta_search), O=player(alphabeta_search)), verbose=True).utility)
        if searchStrategyX == "alpha" and searchStrategyO == "random":
            print(play_game(game, dict(X=player(alphabeta_search), O=random_player), verbose=True).utility)
        if searchStrategyX == "random" and searchStrategyO == "alpha":
            print(play_game(game, dict(X=random_player, O= player(alphabeta_search)), verbose=True).utility)
        if searchStrategyX == "minimax" and searchStrategyO == "random":
            print(play_game(game, dict(X=player(minimax_search), O=random_player), verbose=True).utility)
        if searchStrategyX == "random" and searchStrategyO == "minimax":
            print(play_game(game, dict(X=random_player, O=player(minimax_search)), verbose=True).utility)
        if searchStrategyX == "alpha" and searchStrategyO == "minimax":
            print(play_game(game, dict(X=player(alphabeta_search), O=player(minimax_search)), verbose=True).utility)
        if searchStrategyX == "minimax" and searchStrategyO == "alpha":
            print(play_game(game, dict(X=player(minimax_search), O=player(alphabeta_search)), verbose=True).utility)

        # if searchStrategyX == "random":
        #     X = random_player
        # else:
        #     if searchStrategyX == "alpha":
        #         X = player(alphabeta_search)
        #     else:
        #         if searchStrategyX == "minimax":
        #             X = player(minimax_search)
        #         else: print("not a valid search strategy")
        # if searchStrategyO == "random":
        #     O = random_player
        # else:
        #     if searchStrategyO == "alpha":
        #         O = player(alphabeta_search)
        #     else:
        #         if searchStrategyO == "minimax":
        #             O = player(minimax_search)
        #         else: print("not a valid search strategy")
        # print(X, O)
        # play_game(game, dict(X, O), verbose=True).utility
        """ Prof. Ben's Update """

        response = input("Would you like to run the game again? ('Yes' or 'No').\n").title()

    print("Thank you for Playing Our Game.")

       # if searchStrategyO == "alpha" or searchStrategyX == "alpha" or searchStrategyO == "minimax" or searchStrategyX = "minimax":


        #     search_fn = alphabeta_search
        # elif searchStrategyO == "minimax":
        #     search_fn = minimax_search
        # else:
        #     search_fn = None
        #
        # if search_fn is not None:
        #     game.game(searchStrategyX, search_fn)
        # else:
        #     game.game(searchStrategyX, searchStrategyO)
        # game.game(searchStrategyX, searchStrategyO)
        # state = game.printBoard()
"""
        print("game: ")
        print(game)
        print(game.getGameState())
        state = game.getGameState()
        print("state: ")
        print(state)
        print("print board:")

        print(game.printBoard())


        # check if the game is over
        # winner = game.getWinner()
        # if winner is not None:
        #     if winner == 'T':
        #         print("Game Over: Tie")
        #
        #     else:
        #         print("Game Over: Winner is", winner)
        #         break
"""

if __name__ == "__main__":
    main()



