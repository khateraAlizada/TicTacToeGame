from TicTacToeClass import TicTacToe
def main():
    response = ""
    while response != "No":
        size = input("Enter the size of board game. \n")
        print("\nSize of board game is " + size + "\n")
        searchStrategyO = input("Enter random, alpha, or minimax legal moves search strategy for O. \n")
        searchStrategyX = input("Enter random, alpha, or minimax legal moves search strategy for X. \n")

        print("\nSearch strategy for O is " + searchStrategyO + "\n")
        print("\nSearch strategy for X is " + searchStrategyX + "\n")

        tttObject = TicTacToe(int(size), int(size), int(size))
        print("Search strategy for play X is: " + searchStrategyX)
        print("Search strategy for play O is: " + searchStrategyO)
        # def game(self, searchStrategyX, searchStrategyO):
        print(tttObject.printBoard())
        tttObject.game(searchStrategyX, searchStrategyO)

        response = input("Would you like to run the game again? ('Yes' or 'No') .\n> ").title()
    print("Thank you for Playing Our Game.")


if __name__ == "__main__":
    main()

