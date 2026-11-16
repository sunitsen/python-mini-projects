from game import GuessingGame


def main():
    while True:
        level = input("Difficulty (easy/medium/hard): ").strip().lower()
        try:
            game = GuessingGame.from_difficulty(level)
            break
        except ValueError as err:
            print(err)
    game.play()


if __name__ == "__main__":
    main()
