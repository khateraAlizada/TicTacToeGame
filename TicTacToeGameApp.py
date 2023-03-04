def main():
    response = ""
    while response != "No":
        size = input("Enter the size of board game. \n")
        print("\nSize of board game is " + size + "\n")
        searchStrategyO = input("Enter random, alpha, or minimax legal moves strategy for O. \n")
        searchStrategyX = input("Enter random, alpha, or minimax legal moves strategy for X. \n")

        print("\nSearch strategy for O is " + searchStrategyO + "\n")
        print("\nSearch strategy for X is " + searchStrategyX + "\n")

        response = input("Would you like to run the game again? ('Yes' or 'No') .\n> ")
    print("Thank you for Playing Our Game.")


if __name__ == "__main__":
    main()

