def feed(state, size):
    size[0] += 1
    print("Fish fed")
    if size[0] == 5:
        state[0] = "FISH"


def main():
    state = ["Fish"]
    size = [1]
    print(f"{state[0]} is of size {size[0]}")

    while state[0] != "FISH":
        feed(state, size)

    print(f"It is now a big {state[0]}")


if __name__ == "__main__":
    main()




