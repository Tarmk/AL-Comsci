class Animal:
    def __init__(self, s: str, n: int) -> None:
        self.__state: str = s
        self.__size: int = n

    def feed(self) -> None:
        self.__size += 1
        if self.__size == 5:
            self.__state = "FISH"

    def getState(self) -> str:
        return self.__state

    def getSize(self) -> int:
        return self.__size


def main() -> None:
    thisFish = Animal("Fish", 1)

    # First two OUTPUT lines in the pseudocode
    print(f"{thisFish.getState()} is of size {thisFish.getSize()}")

    while thisFish.getState() != "FISH":
        thisFish.feed()

    print(f"It is now a big {thisFish.getState()}")


if __name__ == "__main__":
    main()




